from .lib import (
    _PandasConvertible as _PandasConvertible
)
from pyarrow_stubs_ext.array_common import (
    CommonArray,
    ChunkedArrayT,
)


class Array(_PandasConvertible, CommonArray):
    """
    Array()

        The base class for all Arrow arrays.
    """
    ...


# Default to Array. Anything else needs to use ChunkedArrayT
class ChunkedArray(ChunkedArrayT[Array]):
    """
    ChunkedArray()

        An array-like composed from a (possibly empty) collection of pyarrow.Arrays

        Warnings
        --------
        Do not call this class's constructor directly.

        Examples
        --------
        To construct a ChunkedArray object use :func:`pyarrow.chunked_array`:

        >>> import pyarrow as pa
        >>> pa.chunked_array([], type=pa.int8())
        <pyarrow.lib.ChunkedArray object at ...>
        [
        ...
        ]

        >>> pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        <pyarrow.lib.ChunkedArray object at ...>
        [
          [
            2,
            2,
            4
          ],
          [
            4,
            5,
            100
          ]
        ]
        >>> isinstance(pa.chunked_array([[2, 2, 4], [4, 5, 100]]), pa.ChunkedArray)
        True
    """
