import pandas as pd
import matplotlib as plt
import numpy as np
#import seaborn as sb
import cupy as cp
#import cuml as cm
import os

UNIQUE_CELLS : any
UNIQUE_GENES : any
DATA : any
GPU_MATRIX : any

def midcount_filling() -> cp.ndarray:
    gpu_matrix = cp.zeros((len(UNIQUE_CELLS), len(UNIQUE_GENES)), dtype=cp.uint8)

    cell_indices = pd.factorize(DATA['CellID'])[0] 
    gene_indices = pd.factorize(DATA['geneID'])[0]

    gpu_cell_indices = cp.array(cell_indices, dtype=cp.uint16)
    gpu_gene_indices = cp.array(gene_indices, dtype=cp.uint16)

    gpu_midcount = cp.array(DATA['MIDCount'].values, dtype=cp.uint8)
    gpu_matrix[gpu_cell_indices, gpu_gene_indices] = gpu_midcount

    tmp_matrix = cp.asnumpy(gpu_matrix)
    unloged_matrix = pd.DataFrame(tmp_matrix, index=UNIQUE_CELLS, columns=UNIQUE_GENES, dtype=np.uint8)
    unloged_matrix.to_csv('sd1_nolog.csv', index=False)

    return gpu_matrix

def matrix_log(gpu_matrix : cp.ndarray) -> cp.ndarray:
    gpu_matrix = gpu_matrix.astype(cp.float32)
    gpu_matrix[gpu_matrix == 0] = -1
    gpu_matrix = cp.where(data == -1, -1, cp.log(gpu_matrix))

    tmp_matrix = cp.asnumpy(gpu_matrix)
    loged_matrix = pd.DataFrame(tmp_matrix, index=UNIQUE_CELLS, columns=UNIQUE_GENES, dtype=np.float32)
    loged_matrix.to_csv('sd1_log.csv', index=False)


data = pd.read_csv('sd0.csv', index_col=0)
data.reset_index(inplace=True, drop=True)

data['CellID'] = data['CellID'].astype(np.uint16)
data['ExonCount'] = data['ExonCount'].astype(np.uint8)
data['MIDCount'] = data['MIDCount'].astype(np.uint8)
data['x'] = data['x'].astype(np.uint16)
data['y'] = data['y'].astype(np.uint16)

UNIQUE_CELLS = data['CellID'].unique()
UNIQUE_GENES = data['geneID'].unique()
DATA = data

data.to_csv('sd1.csv', index=False)

print(f'starting midcount filling\n')
GPU_MATRIX = midcount_filling()
print(f'finished midcount filling, starting matrix loging\n')
GPU_MATRIX = matrix_log(GPU_MATRIX)
print(f'finished matrix loging\n')