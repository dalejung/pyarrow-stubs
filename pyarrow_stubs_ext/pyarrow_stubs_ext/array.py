from typing import (
    Any,
    Callable,
    TypeVar,
    Tuple,
    Union,
    TYPE_CHECKING,
)

import pyarrow as pa


PaDataT = TypeVar('PaDataT', bound=pa.Array | pa.ChunkedArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=pa.Array | pa.ChunkedArray)
