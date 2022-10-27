from typing import (
    TypeVar,
)
import pyarrow as pa

PaChunkedStructArray = pa.ChunkedArray[pa.StructArray, pa.StructType]
PaArray = pa.Array | pa.ChunkedArray
PaStructArray = pa.StructArray | PaChunkedStructArray

PaDataT = TypeVar('PaDataT', bound=PaArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=PaArray)
