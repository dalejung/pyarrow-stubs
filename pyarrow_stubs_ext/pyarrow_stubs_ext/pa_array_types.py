from typing import (
    TypeVar,
    TYPE_CHECKING,
)
import pyarrow as pa

PaArray = pa.Array | pa.ChunkedArray

if TYPE_CHECKING:
    PaChunkedStructArray = pa.ChunkedArray[pa.StructArray, pa.StructType]
    PaStructArray = pa.StructArray | PaChunkedStructArray

PaDataT = TypeVar('PaDataT', bound=PaArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=PaArray)
