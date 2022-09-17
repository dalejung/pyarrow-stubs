from typing import TypeVar, Generic, Iterator
from typing_extensions import Self

import numpy as np
from pyarrow.lib import (
    _PandasConvertible as _PandasConvertible
)

T = TypeVar('T')


class CommonArray:
    def __array__(self) -> np.ndarray:
        ...

    def __iter__(self) -> Iterator:
        ...

    def to_pylist(self) -> list:
        ...

    def to_numpy(self, zero_copy_only=..., writable=...) -> np.ndarray:
        ...

    def __getitem__(self, k):
        ...

    def fill_null(self, fill_value) -> Self:
        ...


class ChunkedArrayT(_PandasConvertible, CommonArray, Generic[T]):
    chunks: list[T]

    def combine_chunks(self) -> T:
        ...
