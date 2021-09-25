# Benchmarks for Python structural matching

CPU: `AMD® Ryzen 7 pro 3700u w/ radeon vega mobile gfx × 8`

CPython built from commit `58f8adfda3`.

```
$ ../cpython/python -m timeit -s 'import matchtypes' 'matchtypes.pattern_matching({})'
500000 loops, best of 5: 833 nsec per loop
```

```
$ ../cpython/python -m timeit -s 'import matchtypes' 'matchtypes.ifelse({})'
500000 loops, best of 5: 598 nsec per loop
```

```
$ ../cpython/python -m timeit -s 'import matchints' 'matchints.pattern_matching({})'
1000000 loops, best of 5: 277 nsec per loop
```

```
$ ../cpython/python -m timeit -s 'import matchints' 'matchints.ifelse({})'
1000000 loops, best of 5: 249 nsec per loop
```

```
# Variant of matchtypes test that gradually increases the number of match
# conditions. We see that both scale linearly.
$ bash curve_matchtypes.sh
1; 240; 270
100; 8.14e+03; 1.45e+04
1000; 2.39e+05; 1.75e+05
10000; 1.08e+06; 1.53e+06
```
