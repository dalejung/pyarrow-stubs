from .lib import (
    _Weakrefable as _Weakrefable,
    DataType as DataType,
)


class Scalar(_Weakrefable):
    """
    Scalar()

        The base class for scalars.
    """
    ...
    type: DataType

    def as_py(self):
        ...
