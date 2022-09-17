from .lib import (
    _Weakrefable as _Weakrefable,
)


class Field(_Weakrefable):
    """
    Field()

        A named field, with a data type, nullability, and optional metadata.

        Notes
        -----
        Do not use this class's constructor directly; use pyarrow.field
    """
    ...
