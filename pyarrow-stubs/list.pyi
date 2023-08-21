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
    ...


class ListArray(BaseListArray):
    """
    Concrete class for Arrow arrays of a list data type.
    """
    type: ListType

    def __getitem__(self, key) -> ListScalar:
        ...
