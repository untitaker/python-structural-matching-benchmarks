extract_timing() {
    tail -1 | cut -d' ' -f6
}

for i in 1 100 1000 10000; do
    echo -n "$i; "
    echo -n $(../cpython/python -m timeit -u nsec -s "import generate_matchtypes; x = generate_matchtypes.generate_pattern_matching(${i})" 'x({})' | extract_timing)
    echo -n "; "
    echo -n $(../cpython/python -m timeit -u nsec -s "import generate_matchtypes; x = generate_matchtypes.generate_ifelse(${i})" 'x({})' | extract_timing)
    echo
done
