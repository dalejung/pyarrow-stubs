import numpy as np
from typing import TypeVar, Generic
from typing_extensions import Self

from .lib import (
    _Weakrefable as _Weakrefable,
    _PandasConvertible as _PandasConvertible
)


T = TypeVar('T')


class CommonArray:
    def __array__(self) -> np.ndarray:
        ...

    def __iter__(self):
        ...

    def to_pylist(self) -> list:
        ...

    def to_numpy(self, zero_copy_only=True, writable=False) -> np.ndarray:
        ...

    def __getitem__(self, k):
        ...

    def fill_null(self, fill_value) -> Self:
        ...


class Array(_PandasConvertible, CommonArray):
    """
    Array()

        The base class for all Arrow arrays.
    """
    ...


class ChunkedArrayT(_PandasConvertible, CommonArray, Generic[T]):
    chunks: list[T]

    def combine_chunks(self) -> T:
        ...


class ChunkedArray(ChunkedArrayT[Array]):
    """
    ChunkedArray()

        An array-like composed from a (possibly empty) collection of pyarrow.Arrays

        Warnings
        --------
        Do not call this class's constructor directly.

        Examples
        --------
        To construct a ChunkedArray object use :func:`pyarrow.chunked_array`:

        >>> import pyarrow as pa
        >>> pa.chunked_array([], type=pa.int8())
        <pyarrow.lib.ChunkedArray object at ...>
        [
        ...
        ]

        >>> pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            2,
            2,
            4
          ],
          [
            4,
            5,
            100
          ]
        ]
        >>> isinstance(pa.chunked_array([[2, 2, 4], [4, 5, 100]]), pa.ChunkedArray)
        True
    """
