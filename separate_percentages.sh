#!/bin/sh

set -e
set -u

cat data/cloud/comparisons/* | grep -o -e "-\?[0-9.]\+%" > percentage_deltas/cloud
cat data/local/comparisons/* | grep -o -e "-\?[0-9.]\+%" > percentage_deltas/local
