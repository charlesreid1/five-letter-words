#!/bin/bash
set -e

mkdir -p output

SCRIPTS=(
    diff_by_n
    distinct
    euclidean_distance
    letter_coverage
    lexico
    near_palindromes
    palindromes
    reverse_lexico
    stats
    tries
)

for script in "${SCRIPTS[@]}"; do
    echo "Running ${script}.py ..."
    python "${script}.py" > "output/${script}.txt" 2>&1
done

echo "Done. Output files in output/"
