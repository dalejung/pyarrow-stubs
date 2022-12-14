"""
This type stub file was generated by pyright.
"""

_logical_type_map = ...
def get_logical_type_map(): # -> dict[Unknown, Unknown]:
    ...

def get_logical_type(arrow_type): # -> LiteralString | Literal['categorical', 'datetimetz', 'datetime', 'decimal', 'object']:
    ...

_numpy_logical_type_map = ...
def get_logical_type_from_numpy(pandas_collection): # -> str:
    ...

def get_extension_dtype_info(column): # -> tuple[str, dict[str, Unknown] | None]:
    ...

def get_column_metadata(column, name, arrow_type, field_name): # -> dict[str, Unknown]:
    """Construct the metadata for a given column

    Parameters
    ----------
    column : pandas.Series or pandas.Index
    name : str
    arrow_type : pyarrow.DataType
    field_name : str
        Equivalent to `name` when `column` is a `Series`, otherwise if `column`
        is a pandas Index then `field_name` will not be the same as `name`.
        This is the name of the field in the arrow Table's schema.

    Returns
    -------
    dict
    """
    ...

def construct_metadata(columns_to_convert, df, column_names, index_levels, index_descriptors, preserve_index, types): # -> dict[bytes, bytes]:
    """Returns a dictionary containing enough metadata to reconstruct a pandas
    DataFrame as an Arrow Table, including index columns.

    Parameters
    ----------
    columns_to_convert : list[pd.Series]
    df : pandas.DataFrame
    index_levels : List[pd.Index]
    index_descriptors : List[Dict]
    preserve_index : bool
    types : List[pyarrow.DataType]

    Returns
    -------
    dict
    """
    ...

def dataframe_to_types(df, preserve_index, columns=...): # -> tuple[list[Unknown], list[Unknown], dict[bytes, bytes]]:
    ...

def dataframe_to_arrays(df, schema, preserve_index, nthreads=..., columns=..., safe=...): # -> tuple[list[Unknown], Unknown, int | None]:
    ...

def get_datetimetz_type(values, dtype, type_): # -> tuple[Unknown, Unknown]:
    ...

def dataframe_to_serialized_dict(frame): # -> dict[str, list[Unknown]]:
    ...

def serialized_dict_to_dataframe(data):
    ...

def make_datetimetz(tz):
    ...

def table_to_blockmanager(options, table, categories=..., ignore_metadata=..., types_mapper=...):
    ...

_pandas_supported_numpy_types = ...
_pandas_logical_type_map = ...
def make_tz_aware(series, tz):
    """
    Make a datetime64 Series timezone-aware for the given tz
    """
    ...

