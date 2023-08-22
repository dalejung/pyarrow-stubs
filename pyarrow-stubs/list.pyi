from .lib import (
    DataType,
)
from .field import Field
from .array import Array
from .scalar import Scalar


class ListType(DataType):
    """
    Concrete class for list data types.
    """
    value_type: DataType
    value_field: Field


class ListScalar(Scalar):
    """
    Concrete class for list-like scalars.
    """
    values: Array


class BaseListArray(Array):
    def flatten(self) -> Array:
        ...


class ListArray(BaseListArray):
    """
    Concrete class for Arrow arrays of a list data type.
    """
    type: ListType
    values: Array
    offsets: Array

    def __getitem__(self, key) -> ListScalar:
        ...


class MapArray(ListArray):
    """
    Concrete class for Arrow arrays of a map data type.
    """


class LargeListArray(BaseListArray):
    """
    Concrete class for Arrow arrays of a large list data type.

        Identical to ListArray, but 64-bit offsets.
    """
