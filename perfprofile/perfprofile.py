#!/usr/bin/env python3
from argparse import ArgumentParser
import copy
import csv
import json
from itertools import groupby, chain
from math import floor, log10
import os
import sys
from time import time
import profile_strategy
try:
    import yaml
except:
    sys.stderr.write('YAML output not available. Install pyyaml to support yaml output.')


def main():
    parser = ArgumentParser('Runs a relative performance profile')
    parser.add_argument('files', nargs='+')
    parser.add_argument('-o', '--outfile', nargs='*', default=['perfprofile.csv'])
    args = parser.parse_args()

    files_ordered = sorted(args.files, key=lambda f: os.path.basename(f))
    problems = groupby(files_ordered,
                       key=lambda f: os.path.splitext(os.path.basename(f))[0])
    all_results = {}

    print('Bootstrapping docker containers...')
    with print('\tNode 12...') or profile_strategy.Node12Strategy() as js12, \
        print('\tNode 11...') or profile_strategy.Node11Strategy() as js11, \
        print('\tNode 10...') or profile_strategy.Node10Strategy() as js10, \
        print('\tCPython 3...') or profile_strategy.CPython3Strategy() as py3, \
        print('\tCPython 2...') or profile_strategy.CPython2Strategy() as py2, \
        print('\tPyPy 3...') or profile_strategy.PyPy3Strategy() as pypy3, \
        print('\tPyPy 2...') or profile_strategy.PyPy2Strategy() as pypy2, \
        print('\tRuby...') or profile_strategy.RubyStrategy() as rb, \
        print('\tGolang...') or profile_strategy.GoStrategy() as go, \
        print('\tC#.NET...') or profile_strategy.CSharpDotNetCoreStrategy() as cscore, \
        print('\tKotlin...') or profile_strategy.KotlinStrategy() as kt:

        strategies = [js12, js11, js10, py3, py2, pypy3, pypy2, rb, go, cscore, kt]

        print('Bootstrapping profiler...')
        go.exec(['go', 'build', '-o', 'perfprofile/profile.bin', 'perfprofile/profile.go'])

        for problem, files in problems:
            print('Profiling {}'.format(problem))
            start = time()
            all_results[problem] = {}
            for f in files:
                ext = os.path.splitext(f)[1]
                strats_for_file = [
                    s for s in strategies
                    if s.matches_file(f)
                ]
                strat_names = [s.name for s in strats_for_file]

                print('\tProfiling {} using strategies {}'.format(f, strat_names))
                results = {
                    strat.name: strat.get_perf_profile(f)
                    for strat in strats_for_file
                }
                all_results[problem].update(results)
            end = time()
            elapsed = int(end - start)
            print('Finished profiling {} in {} seconds.'.format(problem, elapsed))

    print()

    for breakdown in all_results.values():
        for strat_name, result in breakdown.items():
            breakdown[strat_name] = result

    for outfile in args.outfile:
        print('Writing {}'.format(outfile))
        ext = os.path.splitext(outfile)[1].lower()
        if ext in {'.json'}:
            output_json(all_results, outfile)
        elif ext in {'.yml', '.yaml'}:
            output_yaml(all_results, outfile)
        elif ext in {'.csv'}:
            output_csv(all_results, outfile)
        elif ext in {'.md'}:
            output_markdown(all_results, outfile)


def output_json(results, outfile, **kwargs):
    with open(outfile, 'w') as jsonfile:
        json.dump(results, jsonfile, indent=4, **kwargs)


def output_yaml(results, outfile, **kwargs):
    with open(outfile, 'w') as yamlfile:
        yaml.dump(results, yamlfile, default_flow_style=False, **kwargs)


def output_csv(results, outfile):
    headers = ['Problem']
    headers += list(sorted(set(chain.from_iterable(problem.keys()
                                                   for problem in results.values()))))

    with open(outfile, 'w') as csvfile:
        for title, selector in [
                    ('Clock Time (s)', 'Average'),
                    ('Memory (B)', 'AverageMem'),
                    ('User Time (s)', 'AverageUTime'),
                    ('System Time (s)', 'AverageSTime')
                ]:
            csvfile.write('\n{}\n'.format(title))
            writer = csv.DictWriter(csvfile, headers)
            writer.writeheader()
            for problem, resultset in results.items():
                to_write = {problem: result[selector] for problem, result in resultset.items()}
                to_write['Problem'] = problem
                writer.writerow(to_write)


def output_markdown(results, outfile):
    headers = ['Problem']
    headers += list(sorted(set(chain.from_iterable(problem.keys()
                                                   for problem in results.values()))))
    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, headers, delimiter='|')
        for title, selector in [
            ('Clock Time (s)', 'Average'),
            ('Memory (B)', 'AverageMem'),
            ('User Time (s)', 'AverageUTime'),
            ('System Time (s)', 'AverageSTime')
        ]:
            csvfile.write('\n\n# {}\n\n'.format(title))
            writer.writeheader()
            writer.writerow({header: '---' for header in headers})
            for problem, resultset in results.items():
                formatter = '{}'
                cast = int
                if any(isinstance(result[selector], float) for result in resultset.values()):
                    formatter = '{:.05}'
                    cast = float

                to_write = {problem: formatter.format(cast(result[selector]))
                            for problem, result in resultset.items()}
                to_write['Problem'] = problem
                writer.writerow(to_write)


if __name__ == '__main__':
    main()
