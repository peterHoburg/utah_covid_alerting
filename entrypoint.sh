#!/usr/bin/env bash

if [ "$DEV" == "true" ]; then
  export PYTHONDEVMODE=1
  export PYTHONTRACEMALLOC=1
fi

exec $@
