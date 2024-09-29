import pandas as pd
import matplotlib as plt
import numpy as np
import seaborn as sb
import cupy as cp
import cuml as cm
from cuml.cluster import HDBSCAN
import os

def clustering() -> None:
    print(f'Starting to load matrix')
    loged_matrix = pd.read_csv('loged_matrix.csv', index_col=0, nrows=16000)
    print(f'Finished loading matrix')
    print(f'Converting matrix to cp.array')
    data = cp.array(loged_matrix.values)
    print(f'Finished conversion')

    hdbscan = HDBSCAN(min_cluster_size=100)
    print(f'Fitting data')
    hdbscan.fit(data)
    print(f'Finished fitting data')

clustering()
