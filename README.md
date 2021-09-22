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
