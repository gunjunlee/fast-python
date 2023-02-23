import math
from functools import partial
from concurrent import futures
import multiprocessing as mp

import numpy as np
import numba as nb
import pandas as pd

import rfast

def calc(x):
    val = 1
    for i in range(1, x):
        val += math.exp(1 / i)
    return val

def np_calc(x):
    val = 1
    val = np.add.reduce(np.exp(1. / np.arange(1, x)))

    return val

@nb.jit(nopython=True)
def nb_calc(x):
    val = 1
    for i in range(1, x):
        val += math.exp(1 / i)
    return val

@nb.jit(nopython=True, nogil=True)
def nb_ng_calc(x):
    val = 1
    for i in range(1, x):
        val += math.exp(1 / i)
    return val

@nb.jit(nopython=True, nogil=True, parallel=True)
def nb_ng_par_calc(x):
    val = 1
    for i in range(1, x):
        val += math.exp(1 / i)
    return val

def calc_series(s):
    return s.map(calc)

def np_calc_series(s):
    return s.map(np_calc)

def nb_calc_series(s):
    return s.map(nb_calc)

def nb_ng_calc_series(s):
    return s.map(nb_ng_calc)

def nb_ng_par_calc_series(s):
    return s.map(nb_ng_par_calc)

def r_calc_series(s):
    return s.map(rfast.r_calc)

def calc_series_one(so, func):
    return so.map(func)

def nb_calc_mp_series(s, w=2):
    ss = np.array_split(s, w)
    with mp.Pool(w) as pool:
        rs = pool.map(partial(calc_series_one, func=nb_calc), ss)
    r = pd.concat(rs)
    return r

def nb_calc_mt_series(s, w=2):
    ss = np.array_split(s, w)

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(calc_series_one, so, nb_calc) for so in ss]

    rs = []
    for f in futures.as_completed(results):
        rs.append(f.result())

    r = pd.concat(rs)
    return r

def nb_ng_calc_mt_series(s, w=2):
    ss = np.array_split(s, w)

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(calc_series_one, so, nb_ng_calc) for so in ss]

    rs = []
    for f in futures.as_completed(results):
        rs.append(f.result())

    r = pd.concat(rs)
    return r

def r_calc_mt_series(s, w=2):
    ss = np.array_split(s, w)

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(calc_series_one, so, rfast.r_calc) for so in ss]

    rs = []
    for f in futures.as_completed(results):
        rs.append(f.result())

    r = pd.concat(rs)
    return r

def r_ng_calc_mt_series(s, w=2):
    ss = np.array_split(s, w)

    with futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(calc_series_one, so, rfast.r_ng_calc) for so in ss]

    rs = []
    for f in futures.as_completed(results):
        rs.append(f.result())

    r = pd.concat(rs)
    return r
