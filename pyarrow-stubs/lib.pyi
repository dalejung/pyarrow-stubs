class _Weakrefable():
    ...


class _PandasConvertible(_Weakrefable):
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
    ):
        ...


class DataType(_Weakrefable):
    """
    DataType()

        Base class of all Arrow data types.

        Each data type is an *instance* of this class.
    """
    ...
