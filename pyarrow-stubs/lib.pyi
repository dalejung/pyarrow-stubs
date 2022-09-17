class _Weakrefable():
    ...


class _PandasConvertible(_Weakrefable):
    def to_pandas(
        self,
        memory_pool=None,
            categories=None,
            strings_to_categorical=False,
            zero_copy_only=False,
            integer_object_nulls=False,
            date_as_object=True,
            timestamp_as_object=False,
            use_threads=True,
            eduplicate_objects=True,
            ignore_metadata=False,
            safe=True,
            split_blocks=False,
            self_destruct=False,
            types_mapper=None
    ):
        ...


class DataType(_Weakrefable):
    """
    DataType()

        Base class of all Arrow data types.

        Each data type is an *instance* of this class.
    """
    ...
