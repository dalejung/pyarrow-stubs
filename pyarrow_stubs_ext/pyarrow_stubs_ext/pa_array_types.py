from typing import (
    TypeVar,
)
import pyarrow as pa

PaArray = pa.Array | pa.ChunkedArray

PaDataT = TypeVar('PaDataT', bound=PaArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=PaArray)
