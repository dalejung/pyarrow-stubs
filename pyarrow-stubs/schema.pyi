from collections.abc import Iterator

from .lib import (
    _Weakrefable as _Weakrefable,
)
from .field import Field


class Schema(_Weakrefable):
    """
    Schema()

        A named collection of types a.k.a schema. A schema defines the
        column names and types in a record batch or table data structure.
        They also contain metadata about the columns. For example, schemas 
        converted from Pandas contain metadata about their original Pandas 
        types so they can be converted back to the same types.

        Warnings
        --------
        Do not call this class's constructor directly. Instead use
        :func:`pyarrow.schema` factory function which makes a new Arrow
        Schema object.

        Examples
        --------
        Create a new Arrow Schema object:

        >>> import pyarrow as pa
        >>> pa.schema([
        ...     ('some_int', pa.int32()),
        ...     ('some_string', pa.string())
        ... ])
        some_int: int32
        some_string: string

        Create Arrow Schema with metadata:

        >>> pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
    """
    metadata: dict | None
    pandas_metadata: dict | None
    names: list
    types: list

    def with_metadata(self, metadata: dict | None):
        ...

    def __iter__(self) -> Iterator[Field]:
        ...

    def __len__(self) -> int:
        ...

    def to_string(self) -> str:
        ...


def schema(fields, metadata=None):
    """
    Construct pyarrow.Schema from collection of fields.

        Parameters
        ----------
        fields : iterable of Fields or tuples, or mapping of strings to DataTypes
        metadata : dict, default None
            Keys and values must be coercible to bytes.

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.schema([
        ...     ('some_int', pa.int32()),
        ...     ('some_string', pa.string())
        ... ])
        some_int: int32
        some_string: string
        >>> pa.schema([
        ...     pa.field('some_int', pa.int32()),
        ...     pa.field('some_string', pa.string())
        ... ])
        some_int: int32
        some_string: string

        Returns
        -------
        schema : pyarrow.Schema
    """
