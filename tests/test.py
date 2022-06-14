import fast
import numpy as np
import pandas as pd

num_col = 1000
val = [1000] * num_col
s = pd.Series(val)

def test_calc(benchmark):
    result = benchmark(fast.calc_series, s)

def test_np_calc(benchmark):
    result = benchmark(fast.np_calc_series, s)

def test_nb_calc(benchmark):
    result = benchmark(fast.nb_calc_series, s)

def test_nb_ng_calc(benchmark):
    result = benchmark(fast.nb_ng_calc_series, s)

def test_nb_ng_par_calc(benchmark):
    result = benchmark(fast.nb_ng_par_calc_series, s)

def test_r_calc(benchmark):
    result = benchmark(fast.r_calc_series, s)

def test_nb_calc_mp_series(benchmark):
    result = benchmark(fast.nb_calc_mp_series, s)

def test_nb_calc_mt_series(benchmark):
    result = benchmark(fast.nb_calc_mt_series, s)

def test_nb_ng_calc_mt_series(benchmark):
    result = benchmark(fast.nb_ng_calc_mt_series, s)

def test_r_calc_mt_series(benchmark):
    result = benchmark(fast.r_calc_mt_series, s)

def test_r_ng_calc_mt_series(benchmark):
    result = benchmark(fast.r_ng_calc_mt_series, s)
