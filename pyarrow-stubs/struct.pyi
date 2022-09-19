from .array import Array, BooleanArray


class StructArray(Array):
    """
    Concrete class for Arrow arrays of a struct data type.
    """
    def is_valid(self) -> BooleanArray:
        ...
