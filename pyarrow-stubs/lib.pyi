from typing import (
    TypeVar,
    Generic,
)


class _Weakrefable():
    ...


T = TypeVar('T')


class _PandasConvertible(Generic[T], _Weakrefable):
    def to_pandas(
        self,
        memory_pool=...,
            categories=...,
            strings_to_categorical=...,
            zero_copy_only=...,
            integer_object_nulls=...,
            date_as_object=...,
            timestamp_as_object=...,
            use_threads=...,
            eduplicate_objects=...,
            ignore_metadata=...,
            safe=...,
            split_blocks=...,
            self_destruct=...,
            types_mapper=...
    ) -> T:
        ...


class DataType(_Weakrefable):
    """
    DataType()

        Base class of all Arrow data types.

        Each data type is an *instance* of this class.
    """
    ...
