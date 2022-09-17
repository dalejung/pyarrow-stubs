from typing import (
    Any,
    Callable,
    TypeVar,
    Tuple,
    Union,
    TYPE_CHECKING,
)

import pyarrow as pa
from pyarrow.lib import (
    _Weakrefable as _Weakrefable,
    _PandasConvertible as _PandasConvertible
)

PaDataT = TypeVar('PaDataT', bound=pa.Array | pa.ChunkedArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=pa.Array | pa.ChunkedArray)


class ChunkedArrayT():
    ...
