from typing import TypeVar, Generic, Iterator
from typing_extensions import Self

import numpy as np
from pyarrow.lib import (
    _PandasConvertible as _PandasConvertible,
    DataType,
)
import pyarrow as pa
import pyarrow.compute as pa_pc

T = TypeVar('T')


class CommonArray:
    type: DataType

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

    def unique(self) -> pa.Array:
        ...

    def drop_null(self) -> Self:
        ...

    def cast(
        self,
        target_type: pa.DataType = ...,
        safe: bool = ...,
        options: pa_pc.CastOptions = ...
    ) -> Self:
        ...

    def __len__(self) -> int:
        ...

    def is_valid(self) -> pa.BooleanArray:
        ...

    def is_null(self) -> pa.BooleanArray:
        ...

    def equals(self, other: pa.Array) -> bool:
        ...

    def dictionary_encode(self, null_encoding: str = ...) -> pa.DictionaryArray:
        ...
