from .lib import (
    DataType,
)
from .field import Field
from .array import Array


class ListType(DataType):
    """
    Concrete class for list data types.
    """
    value_type: DataType
    value_field: Field


class BaseListArray(Array):
    ...


class ListArray(BaseListArray):
    """
    Concrete class for Arrow arrays of a list data type.
    """
    type: ListType
