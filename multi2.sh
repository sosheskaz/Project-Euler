#!/bin/sh -e

# Set NO_PARALLEL=1 to serialize.

PROJECT_NAME=project-euler
PROBLEM="$1"

cd "$(dirname $0)"

echo "Starting docker-compose..."
COMPOSE_PROJECT_NAME="$PROJECT_NAME" docker-compose up -d 2>/dev/null || exit $?

PROJECT_FILTER="label=com.docker.compose.project=$PROJECT_NAME"
RUNNING_FILTER="status=running"
LANG_SELECTOR='{{.Label "com.docker.compose.service"}}'

echo "Finding supported languages..."
LANGS=$(docker container ls -f "$PROJECT_FILTER" -f "$RUNNING_FILTER" --format "$LANG_SELECTOR" || exit $?)

# This makes it look a bit nicer when run in serial
if which sort >> /dev/null; then
    LANGS=$( (for lang in $LANGS; do echo $lang; done) | sort)
fi

echo "Running..."

if ! which parallel >> /dev/null; then
    NO_PARALLEL=1
    echo "GNU Parallel is not installed. You can install it to speed up $0." >&2
fi

if [ -z "$NO_PARALLEL" ]; then
    # GNU Parallel is used for speeding up development, not for profiling, so it's not usually cited in my writings.
    parallel -j 0 printf "{}:\\\\t" \&\& ./euler "{}" "$PROBLEM" 2\>/dev/null ::: $LANGS
else
    for lang in $LANGS; do
        echo "$lang:\t$(./euler $lang $PROBLEM)"
    done
fi
