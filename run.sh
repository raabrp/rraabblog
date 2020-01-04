#!/bin/bash

# keep track of child processes
trap 'kill %1; kill %2' SIGINT

PORT=8088

echo "http://0.0.0.0:$PORT"

# pelican
pelican -r &

# http server
# xdg-open "http://0.0.0.0:$PORT"
light-server -s public -p "$PORT" -w "** # # reload" > /dev/null
