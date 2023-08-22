from .lib import (
    _Weakrefable
)


class Buffer(_Weakrefable):
    """
    Buffer()

        The base class for all Arrow buffers.

        A buffer represents a contiguous memory area.  Many buffers will own
        their memory, though not all of them do.
    """
    address: int
