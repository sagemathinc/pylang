# Python Microbenchmarks

This is a collection of microbenchmarks to help understand where python-lang
is fast and detect situations where it is 100x slower than it should be
to ensure that it is usable. You can run any particular benchmark foo.py in python-lang,
python3 or pypy or python-wasm by typing:

```sh
$ python-lang foo.py
$ python3 foo.py
$ pypy foo.py
$ python-wasm foo.py
```

Many of these benchmarks are silly microbenchmarks that can be optimized
out with an optimizing compiler, but others are kind of interesting, like
the xgcd's with numbers.

You can run all of the benchmarks via

```sh
$ python-lang all.py
$ python3 all.py
$ pypy all.py
```
