from typing import (
    TypeVar,
)

import pyarrow as pa


PaDataT = TypeVar('PaDataT', bound=pa.Array | pa.ChunkedArray | pa.Table)
PaArrayT = TypeVar('PaArrayT', bound=pa.Array | pa.ChunkedArray)


class CommonArray:
    ...


class ChunkedArrayT():
    ...
