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
    with profile_strategy.LazyJavaScriptStrategy() as js, \
        profile_strategy.LazyPythonStrategy() as py, \
        profile_strategy.LazyRubyStrategy() as rb, \
        profile_strategy.GroovyDirectStrategy() as grv, \
        profile_strategy.GroovyNailgunStrategy() as grvng, \
        profile_strategy.GoRunStrategy() as gor, \
        profile_strategy.CompiledGoStrategy() as goc:

        strategies = [js, py, rb, grv, grvng, gor, goc]

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
            breakdown[strat_name] = round_to_sig_figs(result, 5)

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
        writer = csv.DictWriter(csvfile, headers)
        writer.writeheader()
        for problem, results in results.items():
            to_write = copy.deepcopy([results])
            to_write['Problem'] = problem
            writer.writerow(to_write)


def round_to_sig_figs(value, sig_figs):
    return round(value, -int(floor(log10(abs(value)))) + sig_figs)


def output_markdown(results, outfile):
    headers = ['Problem']
    headers += list(sorted(set(chain.from_iterable(problem.keys()
                                                   for problem in results.values()))))
    with open(outfile, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, headers, delimiter='|')
        writer.writeheader()
        writer.writerow({header: '---' for header in headers})
        for problem, results in results.items():
            to_write = copy.deepcopy(results)
            to_write['Problem'] = problem
            writer.writerow(to_write)




if __name__ == '__main__':
    main()
