from __future__ import annotations
from typing import Generic, TypeVar
from .lib import (
    _PandasConvertible,
    DataType,
)
from .io import (
    Buffer,
)
from pyarrow_stubs_ext import (
    CommonArray,
    PaArrayT as PaArrayT,
)


T = TypeVar('T')
DT = TypeVar('DT')


class Array(_PandasConvertible, CommonArray):
    """
    Array()

        The base class for all Arrow arrays.
    """
    def buffers(self) -> list[None | Buffer]:
        ...

    @staticmethod
    def from_buffers(
        type: DataType,
        length: int,
        buffers: list[Buffer | None],
        null_count: int = -1,
        offset: int = 0,
        children: list[Array] | None = None,
    ) -> Array:
        ...


# Default to Array. Anything else needs to use ChunkedArrayT
# This is wonky due to not having https://peps.python.org/pep-0696/
# Would like to default to Array, DataType but can't do that without changing
# ChunkedArray from being a generic.
class ChunkedArray(_PandasConvertible, CommonArray, Generic[T, DT]):
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
    chunks: list[T]
    type: DT

    def combine_chunks(self) -> T:
        ...

    def iterchunks(self) -> T:
        ...


# Concrete Implementations


class LargeBinaryArray(Array):
    """
    Concrete class for Arrow arrays of large variable-sized binary data type.
    """


class BooleanArray(Array):
    """
    Concrete class for Arrow arrays of boolean data type.
    """


class StringArray(Array):
    """
    Concrete class for Arrow arrays of string (or utf8) data type.
    """


class FixedSizeListArray(Array):
    """
    Concrete class for Arrow arrays of a fixed size list data type.
    """


class NumericArray(Array):
    """
    A base class for Arrow numeric arrays.
    """


class FixedSizeBinaryArray(Array):
    """
    Concrete class for Arrow arrays of a fixed-size binary data type.
    """


class ExtensionArray(Array):
    """
    Concrete class for Arrow extension arrays.
    """


class FloatingPointArray(NumericArray):
    """
    A base class for Arrow floating-point arrays.
    """


class DoubleArray(FloatingPointArray):
    """
    Concrete class for Arrow arrays of float64 data type.
    """


class Date32Array(NumericArray):
    """
    Concrete class for Arrow arrays of date32 data type.
    """


class Date64Array(NumericArray):
    """
    Concrete class for Arrow arrays of date64 data type.
    """


class NullArray(Array):
    """
    Concrete class for Arrow arrays of null data type.
    """


class DictionaryArray(Array):
    """
    Concrete class for dictionary-encoded Arrow arrays.
    """


class BinaryArray(Array):
    """
    Concrete class for Arrow arrays of variable-sized binary data type.
    """


class Decimal256Array(FixedSizeBinaryArray):
    """
    Concrete class for Arrow arrays of decimal256 data type.
    """


class TimestampArray(NumericArray):
    """
    Concrete class for Arrow arrays of timestamp data type.
    """


class Decimal128Array(FixedSizeBinaryArray):
    """
    Concrete class for Arrow arrays of decimal128 data type.
    """


class Time64Array(NumericArray):
    """
    Concrete class for Arrow arrays of time64 data type.
    """


class UnionArray(Array):
    """
    Concrete class for Arrow arrays of a Union data type.
    """


class MonthDayNanoIntervalArray(Array):
    """
    Concrete class for Arrow arrays of interval[MonthDayNano] type.
    """


class LargeStringArray(Array):
    """
    Concrete class for Arrow arrays of large string (or utf8) data type.
    """


class HalfFloatArray(FloatingPointArray):
    """
    Concrete class for Arrow arrays of float16 data type.
    """


class IntegerArray(NumericArray):
    """
    A base class for Arrow integer arrays.
    """


class UInt8Array(IntegerArray):
    """
    Concrete class for Arrow arrays of uint8 data type.
    """


class DurationArray(NumericArray):
    """
    Concrete class for Arrow arrays of duration data type.
    """


class Int8Array(IntegerArray):
    """
    Concrete class for Arrow arrays of int8 data type.
    """


class Int64Array(IntegerArray):
    """
    Concrete class for Arrow arrays of int64 data type.
    """


class UInt64Array(IntegerArray):
    """
    Concrete class for Arrow arrays of uint64 data type.
    """


class Int16Array(IntegerArray):
    """
    Concrete class for Arrow arrays of int16 data type.
    """


class FloatArray(FloatingPointArray):
    """
    Concrete class for Arrow arrays of float32 data type.
    """


class Time32Array(NumericArray):
    """
    Concrete class for Arrow arrays of time32 data type.
    """


class Int32Array(IntegerArray):
    """
    Concrete class for Arrow arrays of int32 data type.
    """


class UInt32Array(IntegerArray):
    """
    Concrete class for Arrow arrays of uint32 data type.
    """


class UInt16Array(IntegerArray):
    """
    Concrete class for Arrow arrays of uint16 data type.
    """
