#!/bin/sh -e

PROJECT_NAME=project-euler
LANG=$1
PROBLEM=$2
COUNT=$3

cd "$(dirname $0)"

PROJECT_FILTER="label=com.docker.compose.project=$PROJECT_NAME"
SERVICE_FILTER="label=com.docker.compose.service=$LANG"
RUNNING_FILTER="status=running"

CONTAINER=$(docker container ls -f "$PROJECT_FILTER" -f "$SERVICE_FILTER" -f "$RUNNING_FILTER" --format '{{.ID}}')

docker exec "$CONTAINER" profile $PROBLEM $COUNT
