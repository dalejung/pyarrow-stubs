from collections.abc import Iterator

from pyarrow_stubs_ext import PaArray
from .lib import (
    DataType as DataType,
)
from .field import Field
from .array import Array, BooleanArray


class StructType(DataType):
    """
    Concrete class for struct data types.

        ``StructType`` supports direct indexing using ``[...]`` (implemented via
        ``__getitem__``) to access its fields.
        It will return the struct field with the given index or name.

        Examples
        --------
        >>> import pyarrow as pa

        Accessing fields using direct indexing:

        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})
        >>> struct_type[0]
        pyarrow.Field<x: int32>
        >>> struct_type['y']
        pyarrow.Field<y: string>

        Accessing fields using ``field()``:

        >>> struct_type.field(1)
        pyarrow.Field<y: string>
        >>> struct_type.field('x')
        pyarrow.Field<x: int32>

        # Creating a schema from the struct type's fields:
        >>> pa.schema(list(struct_type))
        x: int32
        y: string
    """
    def get_field_index(self, name: str) -> int:
        ...

    def __iter__(self) -> Iterator[Field]:
        ...


def struct(fields) -> StructType:
    """
    Create StructType instance from fields.

        A struct is a nested type parameterized by an ordered sequence of types
        (which can all be distinct), called its fields.

        Parameters
        ----------
        fields : iterable of Fields or tuples, or mapping of strings to DataTypes
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.

        Examples
        --------
        >>> import pyarrow as pa
        >>> fields = [
        ...     ('f1', pa.int32()),
        ...     ('f2', pa.string()),
        ... ]
        >>> struct_type = pa.struct(fields)
        >>> struct_type
        StructType(struct<f1: int32, f2: string>)
        >>> fields = [
        ...     pa.field('f1', pa.int32()),
        ...     pa.field('f2', pa.string(), nullable=False),
        ... ]
        >>> pa.struct(fields)
        StructType(struct<f1: int32, f2: string not null>)

        Returns
        -------
        type : DataType
    """


class StructArray(Array):
    """
    Concrete class for Arrow arrays of a struct data type.
    """
    type: StructType

    def is_valid(self) -> BooleanArray:
        ...

    def field(self, index: int | str) -> PaArray:
        ...
