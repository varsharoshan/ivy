# global
import mxnet as mx
from typing import Tuple
from collections import namedtuple


def unique_inverse(
    x: mx.ndarray.ndarray.NDArray,
) -> Tuple[mx.ndarray.ndarray.NDArray, mx.ndarray.ndarray.NDArray]:
    out = namedtuple("unique_inverse", ["values", "inverse_indices"])
    values, inverse_indices = mx.np.unique(x, return_inverse=True)
    return out(values, inverse_indices)


def unique_counts(
    x: mx.ndarray.ndarray.NDArray,
) -> Tuple[mx.ndarray.ndarray.NDArray, mx.ndarray.ndarray.NDArray]:
    uc = namedtuple("uc", ["values", "counts"])
    v, c = mx.unique(x, return_counts=True)
    return uc(v, c)
