#!/bin/sh

set -e
set -u

for x in $(seq 100); do
    cargo benchcmp cloud/separated/bench_${x}_? 2>&1 > "cloud/comparisons/cmp_${x}"
    cargo benchcmp local/data/bench_${x}_? 2>&1 > "local/comparisons/cmp_${x}"
done
