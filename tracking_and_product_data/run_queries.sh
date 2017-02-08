#!/bin/bash -x

for q in $(ls -1 queries); do
  cat queries/$q
  evql -d test -f queries/$q
done
