from collections.abc import Mapping

from .lib import (
    _Weakrefable as _Weakrefable,
    _PandasConvertible as _PandasConvertible,
    DataType as DataType,
)
from .table import (
    Table as Table,
)
from .array import (
    Array as Array,
    ChunkedArray as ChunkedArray,
)
from .struct import (
    StructArray as StructArray,
)
from .schema import (
    schema as schema,
    Schema as Schema,
)
from .scalar import (
    Scalar as Scalar,
)
from .field import (
    Field as Field,
)


def __getattr__(name):
    ...


class _Metadata(_Weakrefable):
    ...


class StopToken():
    ...


class _PandasAPIShim():
    """
    _PandasAPIShim()

        Lazy pandas importer that isolates usages of pandas APIs and avoids
        importing pandas until it's actually needed
    """
    ...


class Transcoder():
    ...


class ArrowException(Exception):
    ...


class _RecordBatchFileReader(_Weakrefable):
    ...


class ArrowKeyError(KeyError, ArrowException):
    ...


class Codec(_Weakrefable):
    """
    Codec(unicode compression, compression_level=None)

        Compression codec.

        Parameters
        ----------
        compression : str
            Type of compression codec to initialize, valid values are: 'gzip',
            'bz2', 'brotli', 'lz4' (or 'lz4_frame'), 'lz4_raw', 'zstd' and
            'snappy'.
        compression_level : int, None
            Optional parameter specifying how aggressively to compress.  The
            possible ranges and effect of this parameter depend on the specific
            codec chosen.  Higher values compress more but typically use more
            resources (CPU/RAM).  Some codecs support negative values.

            gzip
                The compression_level maps to the memlevel parameter of
                deflateInit2.  Higher levels use more RAM but are faster
                and should have higher compression ratios.

            bz2
                The compression level maps to the blockSize100k parameter of
                the BZ2_bzCompressInit function.  Higher levels use more RAM
                but are faster and should have higher compression ratios.

            brotli
                The compression level maps to the BROTLI_PARAM_QUALITY
                parameter.  Higher values are slower and should have higher
                compression ratios.

            lz4/lz4_frame/lz4_raw
                The compression level parameter is not supported and must
                be None

            zstd
                The compression level maps to the compressionLevel parameter
                of ZSTD_initCStream.  Negative values are supported.  Higher
                values are slower and should have higher compression ratios.

            snappy
                The compression level parameter is not supported and must
                be None


        Raises
        ------
        ValueError
            If invalid compression value is passed.
    """
    ...


class MemoryPool(_Weakrefable):
    """
    MemoryPool()

        Base class for memory allocation.

        Besides tracking its number of allocated bytes, a memory pool also
        takes care of the required 64-byte alignment for Arrow data.
    """
    ...


class ArrowTypeError(TypeError, ArrowException):
    ...


class SignalStopHandler():
    ...


class DurationType(DataType):
    """
    Concrete class for duration data types.
    """
    ...


class LoggingMemoryPool(MemoryPool):
    """
    LoggingMemoryPool()
    """
    ...


class SerializedPyObject(_Weakrefable):
    """
    Arrow-serialized representation of Python object.
    """
    ...


class _ExtensionRegistryNanny(_Weakrefable):
    ...


class ProxyMemoryPool(MemoryPool):
    """
    ProxyMemoryPool()

        Memory pool implementation that tracks the number of bytes and
        maximum memory allocated through its direct calls, while redirecting
        to another memory pool.
    """
    ...


class Tensor(_Weakrefable):
    """
    Tensor()

        A n-dimensional array a.k.a Tensor.

        Examples
        --------
        >>> import pyarrow as pa
        >>> import numpy as np
        >>> x = np.array([[2, 2, 4], [4, 5, 100]], np.int32)
        >>> pa.Tensor.from_numpy(x, dim_names=["dim1","dim2"])
        <pyarrow.Tensor>
        type: int32
        shape: (2, 3)
        strides: (12, 4)
    """
    ...


class UnionType(DataType):
    """
    Base class for union data types.
    """
    ...


class SerializationContext(_Weakrefable):
    """
    SerializationContext()
    """
    ...


class TableGroupBy():
    """
    A grouping of columns in a table on which to perform aggregations.

        Parameters
        ----------
        table : pyarrow.Table
            Input table to execute the aggregation on.
        keys : str or list[str]
            Name of the grouped columns.

        Examples
        --------
        >>> import pyarrow as pa
        >>> t = pa.table([
        ...       pa.array(["a", "a", "b", "b", "c"]),
        ...       pa.array([1, 2, 3, 4, 5]),
        ... ], names=["keys", "values"])

        Grouping of columns:

        >>> pa.TableGroupBy(t,"keys")
        <pyarrow.lib.TableGroupBy object at ...>

        Perform aggregations:

        >>> pa.TableGroupBy(t,"keys").aggregate([("values", "sum")])
        pyarrow.Table
        values_sum: int64
        keys: string
        ----
        values_sum: [[3,7,5]]
        keys: [["a","b","c"]]
    """
    ...


class _CRecordBatchWriter(_Weakrefable):
    """
    The base RecordBatchWriter wrapper.

        Provides common implementations of convenience methods. Should not
        be instantiated directly by user code.
    """
    ...


class StringBuilder(_Weakrefable):
    """
    Builder class for UTF8 strings.

        This class exposes facilities for incrementally adding string values and
        building the null bitmap for a pyarrow.Array (type='string').
    """
    ...


class ArrowNotImplementedError(NotImplementedError, ArrowException):
    ...


class SparseCSRMatrix(_Weakrefable):
    """
    SparseCSRMatrix()

        A sparse CSR matrix.
    """
    ...


class SparseCSFTensor(_Weakrefable):
    """
    SparseCSFTensor()

        A sparse CSF tensor.

        CSF is a generalization of compressed sparse row (CSR) index.

        CSF index recursively compresses each dimension of a tensor into a set
        of prefix trees. Each path from a root to leaf forms one tensor
        non-zero index. CSF is implemented with two arrays of buffers and one
        arrays of integers.
    """
    ...


class Message(_Weakrefable):
    """
    Message()

        Container for an Arrow IPC message with metadata and optional body
    """
    ...


class _ReadPandasMixin():
    ...


class LargeListType(DataType):
    """
    Concrete class for large list data types
        (like ListType, but with 64-bit offsets).
    """
    ...


class Buffer(_Weakrefable):
    """
    Buffer()

        The base class for all Arrow buffers.

        A buffer represents a contiguous memory area.  Many buffers will own
        their memory, though not all of them do.
    """
    ...


class SparseCOOTensor(_Weakrefable):
    """
    SparseCOOTensor()

        A sparse COO tensor.
    """
    ...


class DictionaryType(DataType):
    """
    Concrete class for dictionary data types.
    """
    ...


class FixedSizeBinaryType(DataType):
    """
    Concrete class for fixed-size binary data types.
    """
    ...


class ArrowCancelled(ArrowException):
    ...


class Decimal256Type(FixedSizeBinaryType):
    """
    Concrete class for Decimal256 data types.
    """
    ...


class NativeFile(_Weakrefable):
    """
    The base class for all Arrow streams.

        Streams are either readable, writable, or both.
        They optionally support seeking.

        While this class exposes methods to read or write data from Python, the
        primary intent of using a Arrow stream is to pass it to other Arrow
        facilities that will make use of it, such as Arrow IPC routines.

        Be aware that there are subtle differences with regular Python files,
        e.g. destroying a writable Arrow stream without closing it explicitly
        will not flush any pending data.
    """
    ...


class ListType(DataType):
    """
    Concrete class for list data types.
    """
    ...


class MessageReader(_Weakrefable):
    """
    MessageReader()

        Interface for reading Message objects from some source (like an
        InputStream)
    """
    ...


class ArrowIndexError(IndexError, ArrowException):
    ...


class Time32Type(DataType):
    """
    Concrete class for time32 data types.
    """
    ...


class DictionaryMemo(_Weakrefable):
    """
    Tracking container for dictionary-encoded fields.
    """
    ...


class BufferReader(NativeFile):
    """
    BufferReader(obj)

        Zero-copy reader from objects convertible to Arrow buffer.

        Parameters
        ----------
        obj : Python bytes or pyarrow.Buffer
    """
    ...


class FixedSizeBufferWriter(NativeFile):
    """
    A stream writing to a Arrow buffer.
    """
    ...


class RecordBatchReader(_Weakrefable):
    """
    Base class for reading stream of record batches.

        Record batch readers function as iterators of record batches that also
        provide the schema (without the need to get any batches).

        Warnings
        --------
        Do not call this class's constructor directly, use one of the
        ``RecordBatchReader.from_*`` functions instead.

        Notes
        -----
        To import and export using the Arrow C stream interface, use the
        ``_import_from_c`` and ``_export_from_c`` methods. However, keep in mind this
        interface is intended for expert users.

        Examples
        --------
        >>> import pyarrow as pa
        >>> schema = pa.schema([('x', pa.int64())])
        >>> def iter_record_batches():
        ...     for i in range(2):
        ...         yield pa.RecordBatch.from_arrays([pa.array([1, 2, 3])], schema=schema)
        >>> reader = pa.RecordBatchReader.from_batches(schema, iter_record_batches())
        >>> print(reader.schema)
        x: int64
        >>> for batch in reader:
        ...     print(batch)
        pyarrow.RecordBatch
        x: int64
        pyarrow.RecordBatch
        x: int64
    """
    ...


class ArrowInvalid(ValueError, ArrowException):
    ...


class SparseCSCMatrix(_Weakrefable):
    """
    SparseCSCMatrix()

        A sparse CSC matrix.
    """
    ...


class TimestampType(DataType):
    """
    Concrete class for timestamp data types.
    """
    ...


class IpcWriteOptions(_Weakrefable):
    """
    IpcWriteOptions(metadata_version=MetadataVersion.V5, *, bool allow_64bit=False, use_legacy_format=False, compression=None, bool use_threads=True, bool emit_dictionary_deltas=False, bool unify_dictionaries=False)

        Serialization options for the IPC format.

        Parameters
        ----------
        metadata_version : MetadataVersion, default MetadataVersion.V5
            The metadata version to write.  V5 is the current and latest,
            V4 is the pre-1.0 metadata version (with incompatible Union layout).
        allow_64bit : bool, default False
            If true, allow field lengths that don't fit in a signed 32-bit int.
        use_legacy_format : bool, default False
            Whether to use the pre-Arrow 0.15 IPC format.
        compression : str, Codec, or None
            compression codec to use for record batch buffers.
            If None then batch buffers will be uncompressed.
            Must be "lz4", "zstd" or None.
            To specify a compression_level use `pyarrow.Codec`
        use_threads : bool
            Whether to use the global CPU thread pool to parallelize any
            computational tasks like compression.
        emit_dictionary_deltas : bool
            Whether to emit dictionary deltas.  Default is false for maximum
            stream compatibility.
        unify_dictionaries : bool
            If true then calls to write_table will attempt to unify dictionaries
            across all batches in the table.  This can help avoid the need for
            replacement dictionaries (which the file format does not support)
            but requires computing the unified dictionary and then remapping
            the indices arrays.

            This parameter is ignored when writing to the IPC stream format as
            the IPC stream format can support replacement dictionaries.
    """
    ...


class MapType(DataType):
    """
    Concrete class for map data types.
    """
    ...


class ArrowCapacityError(ArrowException):
    ...


class PythonFile(NativeFile):
    """
    A stream backed by a Python file object.

        This class allows using Python file objects with arbitrary Arrow
        functions, including functions written in another language than Python.

        As a downside, there is a non-zero redirection cost in translating
        Arrow stream calls to Python method calls.  Furthermore, Python's
        Global Interpreter Lock may limit parallelism in some situations.
    """
    ...


class IpcReadOptions(_Weakrefable):
    """
    IpcReadOptions(bool ensure_native_endian=True, *, bool use_threads=True, list included_fields=None)

        Serialization options for reading IPC format.

        Parameters
        ----------
        use_threads : bool
            Whether to use the global CPU thread pool to parallelize any
            computational tasks like decompression.
        ensure_native_endian : bool
            Whether to convert incoming data to platform-native endianness.
            Default is true.
        included_fields : list
            If empty (the default), return all deserialized fields.
            If non-empty, the values are the indices of fields to read on
            the top-level schema.
    """
    ...


class ArrowMemoryError(MemoryError, ArrowException):
    ...


class ArrowSerializationError(ArrowException):
    ...


class FixedSizeListType(DataType):
    """
    Concrete class for fixed size list data types.
    """
    ...


class SparseUnionType(UnionType):
    """
    Concrete class for sparse union types.
    """
    ...


class MemoryMappedFile(NativeFile):
    """
    A stream that represents a memory-mapped file.

        Supports 'r', 'r+', 'w' modes.
    """
    ...


class Time64Type(DataType):
    """
    Concrete class for time64 data types.
    """
    ...


class _RecordBatchStreamReader(RecordBatchReader):
    ...


class Time32Scalar(Scalar):
    """
    Concrete class for time32 scalars.
    """
    ...


class StructType(DataType):
    """
    Concrete class for struct data types.

        ``StructType`` supports direct indexing using ``[...]`` (implemented via
        ``__getitem__``) to access its fields.
        It will return the struct field with the given index or name.

        Examples
        --------
        >>> import pyarrow as pa

        Accessing fields using direct indexing:

        >>> struct_type = pa.struct({'x': pa.int32(), 'y': pa.string()})
        >>> struct_type[0]
        pyarrow.Field<x: int32>
        >>> struct_type['y']
        pyarrow.Field<y: string>

        Accessing fields using ``field()``:

        >>> struct_type.field(1)
        pyarrow.Field<y: string>
        >>> struct_type.field('x')
        pyarrow.Field<x: int32>

        # Creating a schema from the struct type's fields:
        >>> pa.schema(list(struct_type))
        x: int32
        y: string
    """
    ...


class BaseExtensionType(DataType):
    """
    Concrete base class for extension types.
    """
    ...


class OSFile(NativeFile):
    """
    A stream backed by a regular file descriptor.
    """
    ...


class BufferedOutputStream(NativeFile):
    """
    BufferedOutputStream(NativeFile stream, int buffer_size, MemoryPool memory_pool=None)

        An output stream that performs buffered reads from
        an unbuffered output stream, which can mitigate the overhead
        of many small writes in some cases.

        Parameters
        ----------
        stream : NativeFile
            The writable output stream to wrap with the buffer
        buffer_size : int
            Size of the buffer that should be added.
        memory_pool : MemoryPool
            The memory pool used to allocate the buffer.
    """
    ...


class UnionScalar(Scalar):
    """
    Concrete class for Union scalars.
    """
    ...


class DoubleScalar(Scalar):
    """
    Concrete class for double scalars.
    """
    ...


class _RecordBatchStreamWriter(_CRecordBatchWriter):
    ...


class DenseUnionType(UnionType):
    """
    Concrete class for dense union types.
    """
    ...


class DeserializationCallbackError(ArrowSerializationError):
    ...


class HalfFloatScalar(Scalar):
    """
    Concrete class for float scalars.
    """
    ...


class CompressedInputStream(NativeFile):
    """
    CompressedInputStream(stream, unicode compression)

        An input stream wrapper which decompresses data on the fly.

        Parameters
        ----------
        stream : string, path, pyarrow.NativeFile, or file-like object
            Input stream object to wrap with the compression.
        compression : str
            The compression type ("bz2", "brotli", "gzip", "lz4" or "zstd").
    """
    ...


class MockOutputStream(NativeFile):
    ...


class ResizableBuffer(Buffer):
    """
    A base class for buffers that can be resized.
    """
    ...


class ExtensionScalar(Scalar):
    """
    Concrete class for Extension scalars.
    """
    ...


class Int8Scalar(Scalar):
    """
    Concrete class for int8 scalars.
    """
    ...


class NullScalar(Scalar):
    """
    NullScalar()

        Concrete class for null scalars.
    """
    ...


class TransformInputStream(NativeFile):
    """
    TransformInputStream(NativeFile stream, transform_func)

        Transform an input stream.

        Parameters
        ----------
        stream : NativeFile
            The stream to transform.
        transform_func : callable
            The transformation to apply.
    """
    ...


class DictionaryScalar(Scalar):
    """
    Concrete class for dictionary-encoded scalars.
    """
    ...


class UInt64Scalar(Scalar):
    """
    Concrete class for uint64 scalars.
    """
    ...


class TimestampScalar(Scalar):
    """
    Concrete class for timestamp scalars.
    """
    ...


class Decimal128Type(FixedSizeBinaryType):
    """
    Concrete class for decimal128 data types.
    """
    ...


class UInt32Scalar(Scalar):
    """
    Concrete class for uint32 scalars.
    """
    ...


class CompressedOutputStream(NativeFile):
    """
    CompressedOutputStream(stream, unicode compression)

        An output stream wrapper which compresses data on the fly.

        Parameters
        ----------
        stream : string, path, pyarrow.NativeFile, or file-like object
            Input stream object to wrap with the compression.
        compression : str
            The compression type ("bz2", "brotli", "gzip", "lz4" or "zstd").
    """
    ...


class Time64Scalar(Scalar):
    """
    Concrete class for time64 scalars.
    """
    ...


class BufferedInputStream(NativeFile):
    """
    BufferedInputStream(NativeFile stream, int buffer_size, MemoryPool memory_pool=None)

        An input stream that performs buffered reads from
        an unbuffered input stream, which can mitigate the overhead
        of many small reads in some cases.

        Parameters
        ----------
        stream : NativeFile
            The input stream to wrap with the buffer
        buffer_size : int
            Size of the temporary read buffer.
        memory_pool : MemoryPool
            The memory pool used to allocate the buffer.
    """
    ...


class BufferOutputStream(NativeFile):
    ...


class Int64Scalar(Scalar):
    """
    Concrete class for int64 scalars.
    """
    ...


class Decimal256Scalar(Scalar):
    """
    Concrete class for decimal256 scalars.
    """
    ...


class Int16Scalar(Scalar):
    """
    Concrete class for int16 scalars.
    """
    ...


class Date64Scalar(Scalar):
    """
    Concrete class for date64 scalars.
    """
    ...


class UInt16Scalar(Scalar):
    """
    Concrete class for uint16 scalars.
    """
    ...


class RecordBatch(_PandasConvertible):
    """
    RecordBatch()

        Batch of rows of columns of equal length

        Warnings
        --------
        Do not call this class's constructor directly, use one of the
        ``RecordBatch.from_*`` functions instead.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]

        Constructing a RecordBatch from arrays:

        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        >>> pa.RecordBatch.from_arrays([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede

        Constructing a RecordBatch from pandas DataFrame:

        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
        ...                    'month': [3, 5, 7, 9],
        ...                    'day': [1, 5, 9, 13],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.RecordBatch.from_pandas(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
        >>> pa.RecordBatch.from_pandas(df).to_pandas()
           year  month  day  n_legs        animals
        0  2020      3    1       2       Flamingo
        1  2022      5    5       4          Horse
        2  2021      7    9       5  Brittle stars
        3  2022      9   13     100      Centipede

        Constructing a RecordBatch from pylist:

        >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'},
        ...           {'n_legs': 4, 'animals': 'Dog'}]
        >>> pa.RecordBatch.from_pylist(pylist).to_pandas()
           n_legs   animals
        0       2  Flamingo
        1       4       Dog

        You can also construct a RecordBatch using :func:`pyarrow.record_batch`:

        >>> pa.record_batch([n_legs, animals], names=names).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede

        >>> pa.record_batch(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
    """
    ...


class Int32Scalar(Scalar):
    """
    Concrete class for int32 scalars.
    """
    ...


class MonthDayNanoIntervalScalar(Scalar):
    """
    Concrete class for month, day, nanosecond interval scalars.
    """
    ...


class SerializationCallbackError(ArrowSerializationError):
    ...


class Date32Scalar(Scalar):
    """
    Concrete class for date32 scalars.
    """
    ...


class BinaryScalar(Scalar):
    """
    Concrete class for binary-like scalars.
    """
    ...


class DurationScalar(Scalar):
    """
    Concrete class for duration scalars.
    """
    ...


class ListScalar(Scalar):
    """
    Concrete class for list-like scalars.
    """
    ...


class ExtensionType(BaseExtensionType):
    """
    ExtensionType(DataType storage_type, extension_name)

        Concrete base class for Python-defined extension types.

        Parameters
        ----------
        storage_type : DataType
        extension_name : str
    """
    ...


class UInt8Scalar(Scalar):
    """
    Concrete class for uint8 scalars.
    """
    ...


class BooleanScalar(Scalar):
    """
    Concrete class for boolean scalars.
    """
    ...


class Decimal128Scalar(Scalar):
    """
    Concrete class for decimal128 scalars.
    """
    ...


class FloatScalar(Scalar):
    """
    Concrete class for float scalars.
    """
    ...


class PyExtensionType(ExtensionType):
    """
    PyExtensionType(DataType storage_type)

        Concrete base class for Python-defined extension types based on pickle
        for (de)serialization.

        Parameters
        ----------
        storage_type : DataType
            The storage type for which the extension is built.
    """
    ...


class UnknownExtensionType(PyExtensionType):
    """
    UnknownExtensionType(DataType storage_type, serialized)

        A concrete class for Python-defined extension types that refer to
        an unknown Python implementation.

        Parameters
        ----------
        storage_type : DataType
            The storage type for which the extension is built.
        serialized : bytes
            The serialised output.
    """
    ...


class _RecordBatchFileWriter(_RecordBatchStreamWriter):
    ...


class FixedSizeListScalar(ListScalar):
    ...


class FixedSizeBinaryScalar(BinaryScalar):
    ...


class StringScalar(BinaryScalar):
    """
    Concrete class for string-like (utf8) scalars.
    """
    ...


class MapScalar(ListScalar):
    """
    Concrete class for map scalars.
    """
    ...


class LargeListScalar(ListScalar):
    ...


class LargeBinaryScalar(BinaryScalar):
    ...


class LargeStringScalar(StringScalar):
    ...


class WriteStats():
    """
    IPC write statistics

        Parameters
        ----------
        num_messages : number of messages.
        num_record_batches : number of record batches.
        num_dictionary_batches : number of dictionary batches.
        num_dictionary_deltas : delta of dictionaries.
        num_replaced_dictionaries : number of replaced dictionaries.
    """
    ...


class KeyValueMetadata(_Metadata, Mapping):
    """
    KeyValueMetadata(__arg0__=None, **kwargs)

        KeyValueMetadata

        Parameters
        ----------
        __arg0__ : dict
            A dict of the key-value metadata
        **kwargs : optional
            additional key-value metadata
    """
    ...


class ReadStats():
    """
    IPC read statistics

        Parameters
        ----------
        num_messages : number of messages.
        num_record_batches : number of record batches.
        num_dictionary_batches : number of dictionary batches.
        num_dictionary_deltas : delta of dictionaries.
        num_replaced_dictionaries : number of replaced dictionaries.
    """
    ...


class StructScalar(Scalar, Mapping):
    """
    Concrete class for struct scalars.
    """
    ...


def allocate_buffer(size: int, memory_pool: MemoryPool | None = None, resizable=False):
    """
    Allocate a mutable buffer.

        Parameters
        ----------
        size : int
            Number of bytes to allocate (plus internal padding)
        memory_pool : MemoryPool, optional
            The pool to allocate memory from.
            If not given, the default memory pool is used.
        resizable : bool, default False
            If true, the returned buffer is resizable.

        Returns
        -------
        buffer : Buffer or ResizableBuffer
    """


def array(
        obj,
        type=None,
        mask=None,
        size=None,
        from_pandas=None,
        safe: bool = True,
        memory_pool: MemoryPool | None = None
) -> Array:
    """
    Create pyarrow.Array instance from a Python object.

        Parameters
        ----------
        obj : sequence, iterable, ndarray or pandas.Series
            If both type and size are specified may be a single use iterable. If
            not strongly-typed, Arrow type will be inferred for resulting array.
        type : pyarrow.DataType
            Explicit type to attempt to coerce to, otherwise will be inferred from
            the data.
        mask : array[bool], optional
            Indicate which values are null (True) or not null (False).
        size : int64, optional
            Size of the elements. If the input is larger than size bail at this
            length. For iterators, if size is larger than the input iterator this
            will be treated as a "max size", but will involve an initial allocation
            of size followed by a resize to the actual size (so if you know the
            exact size specifying it correctly will give you better performance).
        from_pandas : bool, default None
            Use pandas's semantics for inferring nulls from values in
            ndarray-like data. If passed, the mask tasks precedence, but
            if a value is unmasked (not-null), but still null according to
            pandas semantics, then it is null. Defaults to False if not
            passed explicitly by user, or True if a pandas object is
            passed in.
        safe : bool, default True
            Check for overflows or other unsafe conversions.
        memory_pool : pyarrow.MemoryPool, optional
            If not passed, will allocate memory from the currently-set default
            memory pool.

        Returns
        -------
        array : pyarrow.Array or pyarrow.ChunkedArray
            A ChunkedArray instead of an Array is returned if:

            - the object data overflowed binary storage.
            - the object's ``__arrow_array__`` protocol method returned a chunked
              array.

        Notes
        -----
        Timezone will be preserved in the returned array for timezone-aware data,
        else no timezone will be returned for naive timestamps.
        Internally, UTC values are stored for timezone-aware data with the
        timezone set in the data type.

        Pandas's DateOffsets and dateutil.relativedelta.relativedelta are by
        default converted as MonthDayNanoIntervalArray. relativedelta leapdays
        are ignored as are all absolute fields on both objects. datetime.timedelta
        can also be converted to MonthDayNanoIntervalArray but this requires
        passing MonthDayNanoIntervalType explicitly.

        Converting to dictionary array will promote to a wider integer type for
        indices if the number of distinct values cannot be represented, even if
        the index type was explicitly set. This means that if there are more than
        127 values the returned dictionary array's index type will be at least
        pa.int16() even if pa.int8() was passed to the function. Note that an
        explicit index type will not be demoted even if it is wider than required.

        Examples
        --------
        >>> import pandas as pd
        >>> import pyarrow as pa
        >>> pa.array(pd.Series([1, 2]))
        <pyarrow.lib.Int64Array object at ...>
        [
          1,
          2
        ]

        >>> pa.array(["a", "b", "a"], type=pa.dictionary(pa.int8(), pa.string()))
        <pyarrow.lib.DictionaryArray object at ...>
        ...
        -- dictionary:
          [
            "a",
            "b"
          ]
        -- indices:
          [
            0,
            1,
            0
          ]

        >>> import numpy as np
        >>> pa.array(pd.Series([1, 2]), mask=np.array([0, 1], dtype=bool))
        <pyarrow.lib.Int64Array object at ...>
        [
          1,
          null
        ]

        >>> arr = pa.array(range(1024), type=pa.dictionary(pa.int8(), pa.int64()))
        >>> arr.type.index_type
        DataType(int16)
    """


def as_buffer(o):
    """

    """


def asarray(values, type=None):
    """
    Convert to pyarrow.Array, inferring type if not provided.

        Parameters
        ----------
        values : array-like
            This can be a sequence, numpy.ndarray, pyarrow.Array or
            pyarrow.ChunkedArray. If a ChunkedArray is passed, the output will be
            a ChunkedArray, otherwise the output will be a Array.
        type : string or DataType
            Explicitly construct the array with this type. Attempt to cast if
            indicated type is different.

        Returns
        -------
        arr : Array or ChunkedArray
    """


def benchmark_PandasObjectIsNull(obj: list):
    """

    """


def binary(length: int = -1):
    """
    Create variable-length binary type.

        Parameters
        ----------
        length : int, optional, default -1
            If length == -1 then return a variable length binary type. If length is
            greater than or equal to 0 then return a fixed size binary type of
            width `length`.
    """


def bool_():
    """
    Create instance of boolean type.
    """


def chunked_array(arrays, type=None) -> ChunkedArray:
    """
    Construct chunked array from list of array-like objects

        Parameters
        ----------
        arrays : Array, list of Array, or array-like
            Must all be the same data type. Can be empty only if type also passed.
        type : DataType or string coercible to DataType

        Returns
        -------
        ChunkedArray

        Examples
        --------
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
    """


def compress(buf, codec=u'lz4', asbytes=False, memory_pool=None):
    """
    Compress data from buffer-like object.

        Parameters
        ----------
        buf : pyarrow.Buffer, bytes, or other object supporting buffer protocol
        codec : str, default 'lz4'
            Compression codec.
            Supported types: {'brotli, 'gzip', 'lz4', 'lz4_raw', 'snappy', 'zstd'}
        asbytes : bool, default False
            Return result as Python bytes object, otherwise Buffer.
        memory_pool : MemoryPool, default None
            Memory pool to use for buffer allocations, if any.

        Returns
        -------
        compressed : pyarrow.Buffer or bytes (if asbytes=True)
    """


def concat_arrays(arrays, memory_pool: MemoryPool | None = None):
    """
    Concatenate the given arrays.

        The contents of the input arrays are copied into the returned array.

        Raises
        ------
        ArrowInvalid
            If not all of the arrays have the same type.

        Parameters
        ----------
        arrays : iterable of pyarrow.Array
            Arrays to concatenate, must be identically typed.
        memory_pool : MemoryPool, default None
            For memory allocations. If None, the default pool is used.

        Examples
        --------
        >>> import pyarrow as pa
        >>> arr1 = pa.array([2, 4, 5, 100])
        >>> arr2 = pa.array([2, 4])
        >>> pa.concat_arrays([arr1, arr2])
        <pyarrow.lib.Int64Array object at ...>
        [
          2,
          4,
          5,
          100,
          2,
          4
        ]
    """


def concat_tables(tables, promote: bool = False, memory_pool: MemoryPool | None = None):
    """
    Concatenate pyarrow.Table objects.

        If promote==False, a zero-copy concatenation will be performed. The schemas
        of all the Tables must be the same (except the metadata), otherwise an
        exception will be raised. The result Table will share the metadata with the
        first table.

        If promote==True, any null type arrays will be casted to the type of other
        arrays in the column of the same name. If a table is missing a particular
        field, null values of the appropriate type will be generated to take the
        place of the missing field. The new schema will share the metadata with the
        first table. Each field in the new schema will share the metadata with the
        first table which has the field defined. Note that type promotions may
        involve additional allocations on the given ``memory_pool``.

        Parameters
        ----------
        tables : iterable of pyarrow.Table objects
            Pyarrow tables to concatenate into a single Table.
        promote : bool, default False
            If True, concatenate tables with null-filling and null type promotion.
        memory_pool : MemoryPool, default None
            For memory allocations, if required, otherwise use default pool.

        Examples
        --------
        >>> import pyarrow as pa
        >>> t1 = pa.table([
        ...     pa.array([2, 4, 5, 100]),
        ...     pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        ...     ], names=['n_legs', 'animals'])
        >>> t2 = pa.table([
        ...     pa.array([2, 4]),
        ...     pa.array(["Parrot", "Dog"])
        ...     ], names=['n_legs', 'animals'])
        >>> pa.concat_tables([t1,t2])
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100],[2,4]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"],["Parrot","Dog"]]
    """


def cpu_count():
    """
    Return the number of threads to use in parallel operations.

        The number of threads is determined at startup by inspecting the
        ``OMP_NUM_THREADS`` and ``OMP_THREAD_LIMIT`` environment variables.
        If neither is present, it will default to the number of hardware threads
        on the system. It can be modified at runtime by calling
        :func:`set_cpu_count()`.

        See Also
        --------
        set_cpu_count : Modify the size of this pool.
        io_thread_count : The analogous function for the I/O thread pool.
    """


def create_memory_map(path, size):
    """
    Create a file of the given size and memory-map it.

        Parameters
        ----------
        path : str
            The file path to create, on the local filesystem.
        size : int
            The file size to create.

        Returns
        -------
        mmap : MemoryMappedFile
    """


def date32():
    """
    Create instance of 32-bit date (days since UNIX epoch 1970-01-01).
    """


def date64():
    """
    Create instance of 64-bit date (milliseconds since UNIX epoch 1970-01-01).
    """


def decimal128(precision: int, scale: int = 0):
    """
    Create decimal type with precision and scale and 128-bit width.

        Arrow decimals are fixed-point decimal numbers encoded as a scaled
        integer.  The precision is the number of significant digits that the
        decimal type can represent; the scale is the number of digits after
        the decimal point (note the scale can be negative).

        As an example, ``decimal128(7, 3)`` can exactly represent the numbers
        1234.567 and -1234.567 (encoded internally as the 128-bit integers
        1234567 and -1234567, respectively), but neither 12345.67 nor 123.4567.

        ``decimal128(5, -3)`` can exactly represent the number 12345000
        (encoded internally as the 128-bit integer 12345), but neither
        123450000 nor 1234500.

        If you need a precision higher than 38 significant digits, consider
        using ``decimal256``.

        Parameters
        ----------
        precision : int
            Must be between 1 and 38
        scale : int

        Returns
        -------
        decimal_type : Decimal128Type
    """


def decimal256(precision: int, scale: int = 0):
    """
    Create decimal type with precision and scale and 256-bit width.

        Arrow decimals are fixed-point decimal numbers encoded as a scaled
        integer.  The precision is the number of significant digits that the
        decimal type can represent; the scale is the number of digits after
        the decimal point (note the scale can be negative).

        For most use cases, the maximum precision offered by ``decimal128``
        is sufficient, and it will result in a more compact and more efficient
        encoding.  ``decimal256`` is useful if you need a precision higher
        than 38 significant digits.

        Parameters
        ----------
        precision : int
            Must be between 1 and 76
        scale : int

        Returns
        -------
        decimal_type : Decimal256Type
    """


def decompress(buf, decompressed_size=None, codec=u'lz4', asbytes=False, memory_pool=None):
    """
    Decompress data from buffer-like object.

        Parameters
        ----------
        buf : pyarrow.Buffer, bytes, or memoryview-compatible object
            Input object to decompress data from.
        decompressed_size : int, default None
            If not specified, will be computed if the codec is able to determine
            the uncompressed buffer size.
        codec : str, default 'lz4'
            Compression codec.
            Supported types: {'brotli, 'gzip', 'lz4', 'lz4_raw', 'snappy', 'zstd'}
        asbytes : bool, default False
            Return result as Python bytes object, otherwise Buffer.
        memory_pool : MemoryPool, default None
            Memory pool to use for buffer allocations, if any.

        Returns
        -------
        uncompressed : pyarrow.Buffer or bytes (if asbytes=True)
    """


def default_memory_pool():
    """
    Return the process-global memory pool.
    """


def dense_union(child_fields, type_codes=None):
    """
    Create DenseUnionType from child fields.

        A dense union is a nested type where each logical value is taken from
        a single child, at a specific offset.  A buffer of 8-bit type ids
        indicates which child a given logical value is to be taken from,
        and a buffer of 32-bit offsets indicates at which physical position
        in the given child array the logical value is to be taken from.

        Unlike a sparse union, a dense union allows encoding only the child array
        values which are actually referred to by the union array.  This is
        counterbalanced by the additional footprint of the offsets buffer, and
        the additional indirection cost when looking up values.

        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        type_codes : list of integers, default None

        Returns
        -------
        type : DenseUnionType
    """


def deserialize(obj, context: SerializationContext | None = None):
    """
    DEPRECATED: Deserialize Python object from Buffer or other Python
        object supporting the buffer protocol.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        This only can interact with data produced by pyarrow.serialize or
        pyarrow.serialize_to.

        Parameters
        ----------
        obj : pyarrow.Buffer or Python object supporting buffer protocol
        context : SerializationContext
            Custom serialization and deserialization context.

        Returns
        -------
        deserialized : object
    """


def deserialize_components(components, context: SerializationContext | None = None):
    """
    DEPRECATED: Reconstruct Python object from output of
        SerializedPyObject.to_components.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        Parameters
        ----------
        components : dict
            Output of SerializedPyObject.to_components
        context : SerializationContext, default None

        Returns
        -------
        object : the Python object that was originally serialized
    """


def deserialize_from(source, base, context: SerializationContext | None = None):
    """
    DEPRECATED: Deserialize a Python sequence from a file.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        This only can interact with data produced by pyarrow.serialize or
        pyarrow.serialize_to.

        Parameters
        ----------
        source : NativeFile
            File to read the sequence from.
        base : object
            This object will be the base object of all the numpy arrays
            contained in the sequence.
        context : SerializationContext
            Custom serialization and deserialization context.

        Returns
        -------
        object
            Python object for the deserialized sequence.
    """


def dictionary(index_type, value_type, ordered: bool = False):
    """
    Dictionary (categorical, or simply encoded) type.

        Parameters
        ----------
        index_type : DataType
        value_type : DataType
        ordered : bool

        Returns
        -------
        type : DictionaryType
    """


def duration(unit):
    """
    Create instance of a duration type with unit resolution.

        Parameters
        ----------
        unit : str
            One of 's' [second], 'ms' [millisecond], 'us' [microsecond], or
            'ns' [nanosecond].

        Returns
        -------
        type : pyarrow.DurationType

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.duration('us')
        DurationType(duration[us])
        >>> pa.duration('s')
        DurationType(duration[s])
    """


def enable_signal_handlers(enable: bool):
    """
    Enable or disable interruption of long-running operations.

        By default, certain long running operations will detect user
        interruptions, such as by pressing Ctrl-C.  This detection relies
        on setting a signal handler for the duration of the long-running
        operation, and may therefore interfere with other frameworks or
        libraries (such as an event loop).

        Parameters
        ----------
        enable : bool
            Whether to enable user interruption by setting a temporary
            signal handler.
    """


def encode_file_path(path):
    """

    """


def ensure_metadata(meta, allow_none: bool = False):
    """

    """


def ensure_type(ty, allow_none: bool = False):
    """

    """


def field(name, type, nullable: bool = True, metadata=None):
    """
    Create a pyarrow.Field instance.

        Parameters
        ----------
        name : str or bytes
            Name of the field.
        type : pyarrow.DataType
            Arrow datatype of the field.
        nullable : bool, default True
            Whether the field's values are nullable.
        metadata : dict, default None
            Optional field metadata, the keys and values must be coercible to
            bytes.

        Returns
        -------
        field : pyarrow.Field
    """


def float16():
    """
    Create half-precision floating point type.
    """


def float32():
    """
    Create single-precision floating point type.
    """


def float64():
    """
    Create double-precision floating point type.
    """


def foreign_buffer(address, size, base=None):
    """
    Construct an Arrow buffer with the given *address* and *size*.

        The buffer will be optionally backed by the Python *base* object, if given.
        The *base* object will be kept alive as long as this buffer is alive,
        including across language boundaries (for example if the buffer is
        referenced by C++ code).

        Parameters
        ----------
        address : int
            The starting address of the buffer. The address can
            refer to both device or host memory but it must be
            accessible from device after mapping it with
            `get_device_address` method.
        size : int
            The size of device buffer in bytes.
        base : {None, object}
            Object that owns the referenced memory.
    """


def from_numpy_dtype(dtype):
    """
    Convert NumPy dtype to pyarrow.DataType.

        Parameters
        ----------
        dtype : the numpy dtype to convert
    """


def frombytes(o, *, safe=False):
    """
    Decode the given bytestring to unicode.

        Parameters
        ----------
        o : bytes-like
            Input object.
        safe : bool, default False
            If true, raise on encoding errors.
    """


def get_record_batch_size(batch: RecordBatch):
    """
    Return total size of serialized RecordBatch including metadata and padding.

        Parameters
        ----------
        batch : RecordBatch
            The recordbatch for which we want to know the size.
    """


def get_tensor_size(tensor: Tensor):
    """
    Return total size of serialized Tensor including metadata and padding.

        Parameters
        ----------
        tensor : Tensor
            The tensor for which we want to known the size.
    """


def infer_type(values, mask=None, from_pandas=False):
    """
    Attempt to infer Arrow data type that can hold the passed Python
        sequence type in an Array object

        Parameters
        ----------
        values : array-like
            Sequence to infer type from.
        mask : ndarray (bool type), optional
            Optional exclusion mask where True marks null, False non-null.
        from_pandas : bool, default False
            Use pandas's NA/null sentinel values for type inference.

        Returns
        -------
        type : DataType
    """


def input_stream(source, compression=u'detect', buffer_size=None):
    """
    Create an Arrow input stream.

        Parameters
        ----------
        source : str, Path, buffer, file-like object, ...
            The source to open for reading.
        compression : str optional, default 'detect'
            The compression algorithm to use for on-the-fly decompression.
            If "detect" and source is a file path, then compression will be
            chosen based on the file extension.
            If None, no compression will be applied.
            Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").
        buffer_size : int, default None
            If None or 0, no buffering will happen. Otherwise the size of the
            temporary read buffer.
    """


def int16():
    """
    Create instance of signed int16 type.
    """


def int32():
    """
    Create instance of signed int32 type.
    """


def int64():
    """
    Create instance of signed int64 type.
    """


def int8():
    """
    Create instance of signed int8 type.
    """


def io_thread_count():
    """
    Return the number of threads to use for I/O operations.

        Many operations, such as scanning a dataset, will implicitly make
        use of this pool. The number of threads is set to a fixed value at
        startup. It can be modified at runtime by calling
        :func:`set_io_thread_count()`.

        See Also
        --------
        set_io_thread_count : Modify the size of this pool.
        cpu_count : The analogous function for the CPU thread pool.
    """


def is_boolean_value(obj):
    """
    Check if the object is a boolean.

        Parameters
        ----------
        obj : object
            The object to check
    """


def is_float_value(obj):
    """
    Check if the object is a float.

        Parameters
        ----------
        obj : object
            The object to check
    """


def is_integer_value(obj):
    """
    Check if the object is an integer.

        Parameters
        ----------
        obj : object
            The object to check
    """


def is_named_tuple(cls):
    """
    Return True if cls is a namedtuple and False otherwise.
    """


def jemalloc_memory_pool():
    """
    Return a memory pool based on the jemalloc heap.

        NotImplementedError is raised if jemalloc support is not enabled.
    """


def jemalloc_set_decay_ms(decay_ms):
    """
    Set arenas.dirty_decay_ms and arenas.muzzy_decay_ms to indicated number of
        milliseconds. A value of 0 (the default) results in dirty / muzzy memory
        pages being released right away to the OS, while a higher value will result
        in a time-based decay. See the jemalloc docs for more information

        It's best to set this at the start of your application.

        Parameters
        ----------
        decay_ms : int
            Number of milliseconds to set for jemalloc decay conf parameters. Note
            that this change will only affect future memory arenas
    """


def large_binary():
    """
    Create large variable-length binary type.

        This data type may not be supported by all Arrow implementations.  Unless
        you need to represent data larger than 2GB, you should prefer binary().
    """


def large_list(value_type):
    """
    Create LargeListType instance from child data type or field.

        This data type may not be supported by all Arrow implementations.
        Unless you need to represent data larger than 2**31 elements, you should
        prefer list_().

        Parameters
        ----------
        value_type : DataType or Field

        Returns
        -------
        list_type : DataType
    """


def large_string():
    """
    Create large UTF8 variable-length string type.

        This data type may not be supported by all Arrow implementations.  Unless
        you need to represent data larger than 2GB, you should prefer string().
    """


def large_utf8():
    """
    Alias for large_string().
    """


def list_(value_type, list_size: int = -1):
    """
    Create ListType instance from child data type or field.

        Parameters
        ----------
        value_type : DataType or Field
        list_size : int, optional, default -1
            If length == -1 then return a variable length list type. If length is
            greater than or equal to 0 then return a fixed size list type.

        Returns
        -------
        list_type : DataType
    """


def log_memory_allocations(enable=True):
    """
    Enable or disable memory allocator logging for debugging purposes

        Parameters
        ----------
        enable : bool, default True
            Pass False to disable logging
    """


def logging_memory_pool(parent: MemoryPool):
    """
    Create and return a MemoryPool instance that redirects to the
        *parent*, but also dumps allocation logs on stderr.

        Parameters
        ----------
        parent : MemoryPool
            The real memory pool that should be used for allocations.
    """


def map_(key_type, item_type, keys_sorted=False):
    """
    Create MapType instance from key and item data types or fields.

        Parameters
        ----------
        key_type : DataType
        item_type : DataType
        keys_sorted : bool

        Returns
        -------
        map_type : DataType
    """


def memory_map(path, mode=u'r'):
    """
    Open memory map at file path. Size of the memory map cannot change.

        Parameters
        ----------
        path : str
        mode : {'r', 'r+', 'w'}, default 'r'
            Whether the file is opened for reading ('r'), writing ('w')
            or both ('r+').

        Returns
        -------
        mmap : MemoryMappedFile
    """


def mimalloc_memory_pool():
    """
    Return a memory pool based on the mimalloc heap.

        NotImplementedError is raised if mimalloc support is not enabled.
    """


def month_day_nano_interval():
    """
    Create instance of an interval type representing months, days and
        nanoseconds between two dates.
    """


def null():
    """
    Create instance of null type.
    """


def nulls(size, type=None, memory_pool: MemoryPool | None = None):
    """
    Create a strongly-typed Array instance with all elements null.

        Parameters
        ----------
        size : int
            Array length.
        type : pyarrow.DataType, default None
            Explicit type for the array. By default use NullType.
        memory_pool : MemoryPool, default None
            Arrow MemoryPool to use for allocations. Uses the default memory
            pool is not passed.

        Returns
        -------
        arr : Array

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.nulls(10)
        <pyarrow.lib.NullArray object at ...>
        10 nulls

        >>> pa.nulls(3, pa.uint32())
        <pyarrow.lib.UInt32Array object at ...>
        [
          null,
          null,
          null
        ]
    """


def output_stream(source, compression=u'detect', buffer_size=None):
    """
    Create an Arrow output stream.

        Parameters
        ----------
        source : str, Path, buffer, file-like object, ...
            The source to open for writing.
        compression : str optional, default 'detect'
            The compression algorithm to use for on-the-fly compression.
            If "detect" and source is a file path, then compression will be
            chosen based on the file extension.
            If None, no compression will be applied.
            Otherwise, a well-known algorithm name must be supplied (e.g. "gzip").
        buffer_size : int, default None
            If None or 0, no buffering will happen. Otherwise the size of the
            temporary write buffer.
    """


def proxy_memory_pool(parent: MemoryPool):
    """
    Create and return a MemoryPool instance that redirects to the
        *parent*, but with separate allocation statistics.

        Parameters
        ----------
        parent : MemoryPool
            The real memory pool that should be used for allocations.
    """


def py_buffer(obj):
    """
    Construct an Arrow buffer from a Python bytes-like or buffer-like object

        Parameters
        ----------
        obj : object
            the object from which the buffer should be constructed.
    """


def read_message(source):
    """
    Read length-prefixed message from file or buffer-like object

        Parameters
        ----------
        source : pyarrow.NativeFile, file-like object, or buffer-like object

        Returns
        -------
        message : Message
    """


def read_record_batch(obj, schema: Schema, dictionary_memo: DictionaryMemo | None = None):
    """
    Read RecordBatch from message, given a known schema. If reading data from a
        complete IPC stream, use ipc.open_stream instead

        Parameters
        ----------
        obj : Message or Buffer-like
        schema : Schema
        dictionary_memo : DictionaryMemo, optional
            If message contains dictionaries, must pass a populated
            DictionaryMemo

        Returns
        -------
        batch : RecordBatch
    """


def read_schema(obj, dictionary_memo: DictionaryMemo | None = None):
    """
    Read Schema from message or buffer

        Parameters
        ----------
        obj : buffer or Message
        dictionary_memo : DictionaryMemo, optional
            Needed to be able to reconstruct dictionary-encoded fields
            with read_record_batch

        Returns
        -------
        schema : Schema
    """


def read_serialized(source, base=None):
    """
    DEPRECATED: Read serialized Python sequence from file-like object.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        Parameters
        ----------
        source : NativeFile
            File to read the sequence from.
        base : object
            This object will be the base object of all the numpy arrays
            contained in the sequence.

        Returns
        -------
        serialized : the serialized data
    """


def read_tensor(source):
    """
    Read pyarrow.Tensor from pyarrow.NativeFile object from current
        position. If the file source supports zero copy (e.g. a memory map), then
        this operation does not allocate any memory. This function not assume that
        the stream is aligned

        Parameters
        ----------
        source : pyarrow.NativeFile

        Returns
        -------
        tensor : Tensor
    """


def record_batch(data, names=None, schema=None, metadata=None):
    """
    Create a pyarrow.RecordBatch from another Python data structure or sequence
        of arrays.

        Parameters
        ----------
        data : pandas.DataFrame, list
            A DataFrame or list of arrays or chunked arrays.
        names : list, default None
            Column names if list of arrays passed as data. Mutually exclusive with
            'schema' argument.
        schema : Schema, default None
            The expected schema of the RecordBatch. If not passed, will be inferred
            from the data. Mutually exclusive with 'names' argument.
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if schema not passed).

        Returns
        -------
        RecordBatch

        See Also
        --------
        RecordBatch.from_arrays, RecordBatch.from_pandas, table

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 2, 4, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Parrot", "Dog", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]

        Creating a RecordBatch from a list of arrays with names:

        >>> pa.record_batch([n_legs, animals], names=names)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        >>> pa.record_batch([n_legs, animals], names=["n_legs", "animals"]).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       2         Parrot
        2       4            Dog
        3       4          Horse
        4       5  Brittle stars
        5     100      Centipede

        Creating a RecordBatch from a list of arrays with names and metadata:

        >>> my_metadata={"n_legs": "How many legs does an animal have?"}
        >>> pa.record_batch([n_legs, animals],
        ...                  names=names,
        ...                  metadata = my_metadata)
        pyarrow.RecordBatch
        n_legs: int64
        animals: string
        >>> pa.record_batch([n_legs, animals],
        ...                  names=names,
        ...                  metadata = my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'How many legs does an animal have?'

        Creating a RecordBatch from a pandas DataFrame:

        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2021, 2022],
        ...                    'month': [3, 5, 7, 9],
        ...                    'day': [1, 5, 9, 13],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.record_batch(df)
        pyarrow.RecordBatch
        year: int64
        month: int64
        day: int64
        n_legs: int64
        animals: string
        >>> pa.record_batch(df).to_pandas()
           year  month  day  n_legs        animals
        0  2020      3    1       2       Flamingo
        1  2022      5    5       4          Horse
        2  2021      7    9       5  Brittle stars
        3  2022      9   13     100      Centipede

        Creating a RecordBatch from a pandas DataFrame with schema:

        >>> my_schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        >>> pa.record_batch(df, my_schema).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
        pandas: ...
        >>> pa.record_batch(df, my_schema).to_pandas()
           n_legs        animals
        0       2       Flamingo
        1       4          Horse
        2       5  Brittle stars
        3     100      Centipede
    """


def register_extension_type(ext_type):
    """
    Register a Python extension type.

        Registration is based on the extension name (so different registered types
        need unique extension names). Registration needs an extension type
        instance, but then works for any instance of the same subclass regardless
        of parametrization of the type.

        Parameters
        ----------
        ext_type : BaseExtensionType instance
            The ExtensionType subclass to register.
    """


def repeat(value, size, memory_pool: MemoryPool | None = None):
    """
    Create an Array instance whose slots are the given scalar.

        Parameters
        ----------
        value : Scalar-like object
            Either a pyarrow.Scalar or any python object coercible to a Scalar.
        size : int
            Number of times to repeat the scalar in the output Array.
        memory_pool : MemoryPool, default None
            Arrow MemoryPool to use for allocations. Uses the default memory
            pool is not passed.

        Returns
        -------
        arr : Array

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.repeat(10, 3)
        <pyarrow.lib.Int64Array object at ...>
        [
          10,
          10,
          10
        ]

        >>> pa.repeat([1, 2], 2)
        <pyarrow.lib.ListArray object at ...>
        [
          [
            1,
            2
          ],
          [
            1,
            2
          ]
        ]

        >>> pa.repeat("string", 3)
        <pyarrow.lib.StringArray object at ...>
        [
          "string",
          "string",
          "string"
        ]

        >>> pa.repeat(pa.scalar({'a': 1, 'b': [1, 2]}), 2)
        <pyarrow.lib.StructArray object at ...>
        -- is_valid: all not null
        -- child 0 type: int64
          [
            1,
            1
          ]
        -- child 1 type: list<item: int64>
          [
            [
              1,
              2
            ],
            [
              1,
              2
            ]
          ]
    """


def runtime_info():
    """
    Get runtime information.

        Returns
        -------
        info : pyarrow.RuntimeInfo
    """


def scalar(value, type=None, *, from_pandas=None, memory_pool: MemoryPool | None = None):
    """
    Create a pyarrow.Scalar instance from a Python object.

        Parameters
        ----------
        value : Any
            Python object coercible to arrow's type system.
        type : pyarrow.DataType
            Explicit type to attempt to coerce to, otherwise will be inferred from
            the value.
        from_pandas : bool, default None
            Use pandas's semantics for inferring nulls from values in
            ndarray-like data. Defaults to False if not passed explicitly by user,
            or True if a pandas object is passed in.
        memory_pool : pyarrow.MemoryPool, optional
            If not passed, will allocate memory from the currently-set default
            memory pool.

        Returns
        -------
        scalar : pyarrow.Scalar

        Examples
        --------
        >>> import pyarrow as pa

        >>> pa.scalar(42)
        <pyarrow.Int64Scalar: 42>

        >>> pa.scalar("string")
        <pyarrow.StringScalar: 'string'>

        >>> pa.scalar([1, 2])
        <pyarrow.ListScalar: [1, 2]>

        >>> pa.scalar([1, 2], type=pa.list_(pa.int16()))
        <pyarrow.ListScalar: [1, 2]>
    """


def serialize(value, context: SerializationContext | None = None):
    """
    DEPRECATED: Serialize a general Python sequence for transient storage
        and transport.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        Notes
        -----
        This function produces data that is incompatible with the standard
        Arrow IPC binary protocol, i.e. it cannot be used with ipc.open_stream or
        ipc.open_file. You can use deserialize, deserialize_from, or
        deserialize_components to read it.

        Parameters
        ----------
        value : object
            Python object for the sequence that is to be serialized.
        context : SerializationContext
            Custom serialization and deserialization context, uses a default
            context with some standard type handlers if not specified.

        Returns
        -------
        serialized : SerializedPyObject
    """


def serialize_to(value, sink, context: SerializationContext | None = None):
    """
    DEPRECATED: Serialize a Python sequence to a file.

        .. deprecated:: 2.0
            The custom serialization functionality is deprecated in pyarrow 2.0,
            and will be removed in a future version. Use the standard library
            ``pickle`` or the IPC functionality of pyarrow (see :ref:`ipc` for
            more).

        Parameters
        ----------
        value : object
            Python object for the sequence that is to be serialized.
        sink : NativeFile or file-like
            File the sequence will be written to.
        context : SerializationContext
            Custom serialization and deserialization context, uses a default
            context with some standard type handlers if not specified.
    """


def set_cpu_count(count: int):
    """
    Set the number of threads to use in parallel operations.

        Parameters
        ----------
        count : int
            The number of concurrent threads that should be used.

        See Also
        --------
        cpu_count : Get the size of this pool.
        set_io_thread_count : The analogous function for the I/O thread pool.
    """


def set_io_thread_count(count: int):
    """
    Set the number of threads to use for I/O operations.

        Many operations, such as scanning a dataset, will implicitly make
        use of this pool.

        Parameters
        ----------
        count : int
            The max number of threads that may be used for I/O.
            Must be positive.

        See Also
        --------
        io_thread_count : Get the size of this pool.
        set_cpu_count : The analogous function for the CPU thread pool.
    """


def set_memory_pool(pool: MemoryPool):
    """
    Set the default memory pool.

        Parameters
        ----------
        pool : MemoryPool
            The memory pool that should be used by default.
    """


def sparse_union(child_fields, type_codes=None):
    """
    Create SparseUnionType from child fields.

        A sparse union is a nested type where each logical value is taken from
        a single child.  A buffer of 8-bit type ids indicates which child
        a given logical value is to be taken from.

        In a sparse union, each child array should have the same length as the
        union array, regardless of the actual number of union values that
        refer to it.

        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        type_codes : list of integers, default None

        Returns
        -------
        type : SparseUnionType
    """


def string():
    """
    Create UTF8 variable-length string type.
    """


def string_to_tzinfo(name):
    """
    Convert a time zone name into a time zone object.

        Supported input strings are:
        * As used in the Olson time zone database (the "tz database" or
          "tzdata"), such as "America/New_York"
        * An absolute time zone offset of the form +XX:XX or -XX:XX, such as +07:30

        Parameters
        ----------
          name: str
            Time zone name.

        Returns
        -------
          tz : datetime.tzinfo
            Time zone object
    """


def struct(fields):
    """
    Create StructType instance from fields.

        A struct is a nested type parameterized by an ordered sequence of types
        (which can all be distinct), called its fields.

        Parameters
        ----------
        fields : iterable of Fields or tuples, or mapping of strings to DataTypes
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.

        Examples
        --------
        >>> import pyarrow as pa
        >>> fields = [
        ...     ('f1', pa.int32()),
        ...     ('f2', pa.string()),
        ... ]
        >>> struct_type = pa.struct(fields)
        >>> struct_type
        StructType(struct<f1: int32, f2: string>)
        >>> fields = [
        ...     pa.field('f1', pa.int32()),
        ...     pa.field('f2', pa.string(), nullable=False),
        ... ]
        >>> pa.struct(fields)
        StructType(struct<f1: int32, f2: string not null>)

        Returns
        -------
        type : DataType
    """


def supported_memory_backends():
    """
    Return a list of available memory pool backends
    """


def system_memory_pool():
    """
    Return a memory pool based on the C malloc heap.
    """


def table(data, names=None, schema=None, metadata=None, nthreads=None) -> Table:
    """
    Create a pyarrow.Table from a Python data structure or sequence of arrays.

        Parameters
        ----------
        data : pandas.DataFrame, dict, list
            A DataFrame, mapping of strings to Arrays or Python lists, or list of
            arrays or chunked arrays.
        names : list, default None
            Column names if list of arrays passed as data. Mutually exclusive with
            'schema' argument.
        schema : Schema, default None
            The expected schema of the Arrow Table. If not passed, will be inferred
            from the data. Mutually exclusive with 'names' argument.
            If passed, the output will have exactly this schema (raising an error
            when columns are not found in the data and ignoring additional data not
            specified in the schema, when data is a dict or DataFrame).
        metadata : dict or Mapping, default None
            Optional metadata for the schema (if schema not passed).
        nthreads : int, default None
            For pandas.DataFrame inputs: if greater than 1, convert columns to
            Arrow in parallel using indicated number of threads. By default,
            this follows :func:`pyarrow.cpu_count` (may use up to system CPU count
            threads).

        Returns
        -------
        Table

        See Also
        --------
        Table.from_arrays, Table.from_pandas, Table.from_pydict

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]

        Construct a Table from arrays:

        >>> pa.table([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]

        Construct a Table from arrays with metadata:

        >>> my_metadata={"n_legs": "Number of legs per animal"}
        >>> pa.table([n_legs, animals], names=names, metadata = my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'

        Construct a Table from pandas DataFrame:

        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.table(df)
        pyarrow.Table
        year: int64
        n_legs: int64
        animals: string
        ----
        year: [[2020,2022,2019,2021]]
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]

        Construct a Table from pandas DataFrame with pyarrow schema:

        >>> my_schema = pa.schema([
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"n_legs": "Number of legs per animal"})
        >>> pa.table(df, my_schema).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'
        pandas: '{"index_columns": [], "column_indexes": [{"name": null, ...

        Construct a Table from chunked arrays:

        >>> n_legs = pa.chunked_array([[2, 2, 4], [4, 5, 100]])
        >>> animals = pa.chunked_array([["Flamingo", "Parrot", "Dog"], ["Horse", "Brittle stars", "Centipede"]])
        >>> table = pa.table([n_legs, animals], names=names)
        >>> table
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,2,4],[4,5,100]]
        animals: [["Flamingo","Parrot","Dog"],["Horse","Brittle stars","Centipede"]]
    """


def table_to_blocks(options, table: Table, categories, extension_columns):
    """

    """


def time32(unit):
    """
    Create instance of 32-bit time (time of day) type with unit resolution.

        Parameters
        ----------
        unit : str
            one of 's' [second], or 'ms' [millisecond]

        Returns
        -------
        type : pyarrow.Time32Type

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.time32('s')
        Time32Type(time32[s])
        >>> pa.time32('ms')
        Time32Type(time32[ms])
    """


def time64(unit):
    """
    Create instance of 64-bit time (time of day) type with unit resolution.

        Parameters
        ----------
        unit : str
            One of 'us' [microsecond], or 'ns' [nanosecond].

        Returns
        -------
        type : pyarrow.Time64Type

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.time64('us')
        Time64Type(time64[us])
        >>> pa.time64('ns')
        Time64Type(time64[ns])
    """


def timestamp(unit, tz=None):
    """
    Create instance of timestamp type with resolution and optional time zone.

        Parameters
        ----------
        unit : str
            one of 's' [second], 'ms' [millisecond], 'us' [microsecond], or 'ns'
            [nanosecond]
        tz : str, default None
            Time zone name. None indicates time zone naive

        Examples
        --------
        >>> import pyarrow as pa
        >>> pa.timestamp('us')
        TimestampType(timestamp[us])
        >>> pa.timestamp('s', tz='America/New_York')
        TimestampType(timestamp[s, tz=America/New_York])
        >>> pa.timestamp('s', tz='+07:30')
        TimestampType(timestamp[s, tz=+07:30])

        Returns
        -------
        timestamp_type : TimestampType
    """


def tobytes(o):
    """
    Encode a unicode or bytes string to bytes.

        Parameters
        ----------
        o : str or bytes
            Input string.
    """


def total_allocated_bytes():
    """
    Return the currently allocated bytes from the default memory pool.
        Other memory pools may not be accounted for.
    """


def transcoding_input_stream(stream, src_encoding, dest_encoding):
    """
    Add a transcoding transformation to the stream.
        Incoming data will be decoded according to ``src_encoding`` and
        then re-encoded according to ``dest_encoding``.

        Parameters
        ----------
        stream : NativeFile
            The stream to which the transformation should be applied.
        src_encoding : str
            The codec to use when reading data data.
        dest_encoding : str
            The codec to use for emitted data.
    """


def type_for_alias(name):
    """
    Return DataType given a string alias if one exists.

        Parameters
        ----------
        name : str
            The alias of the DataType that should be retrieved.

        Returns
        -------
        type : DataType
    """


def tzinfo_to_string(tz):
    """
    Converts a time zone object into a string indicating the name of a time
        zone, one of:
        * As used in the Olson time zone database (the "tz database" or
          "tzdata"), such as "America/New_York"
        * An absolute time zone offset of the form +XX:XX or -XX:XX, such as +07:30

        Parameters
        ----------
          tz : datetime.tzinfo
            Time zone object

        Returns
        -------
          name : str
            Time zone name
    """


def uint16():
    """
    Create instance of unsigned uint16 type.
    """


def uint32():
    """
    Create instance of unsigned uint32 type.
    """


def uint64():
    """
    Create instance of unsigned uint64 type.
    """


def uint8():
    """
    Create instance of unsigned int8 type.
    """


def unify_schemas(schemas):
    """
    Unify schemas by merging fields by name.

        The resulting schema will contain the union of fields from all schemas.
        Fields with the same name will be merged. Note that two fields with
        different types will fail merging.

        - The unified field will inherit the metadata from the schema where
            that field is first defined.
        - The first N fields in the schema will be ordered the same as the
            N fields in the first schema.

        The resulting schema will inherit its metadata from the first input
        schema.

        Parameters
        ----------
        schemas : list of Schema
            Schemas to merge into a single one.

        Returns
        -------
        Schema

        Raises
        ------
        ArrowInvalid :
            If any input schema contains fields with duplicate names.
            If Fields of the same name are not mergeable.
    """


def union(child_fields, mode, type_codes=None):
    """
    Create UnionType from child fields.

        A union is a nested type where each logical value is taken from a
        single child.  A buffer of 8-bit type ids indicates which child
        a given logical value is to be taken from.

        Unions come in two flavors: sparse and dense
        (see also `pyarrow.sparse_union` and `pyarrow.dense_union`).

        Parameters
        ----------
        child_fields : sequence of Field values
            Each field must have a UTF8-encoded name, and these field names are
            part of the type metadata.
        mode : str
            Must be 'sparse' or 'dense'
        type_codes : list of integers, default None

        Returns
        -------
        type : UnionType
    """


def unregister_extension_type(type_name):
    """
    Unregister a Python extension type.

        Parameters
        ----------
        type_name : str
            The name of the ExtensionType subclass to unregister.
    """


def utf8():
    """
    Alias for string().
    """


def write_tensor(tensor: Tensor, dest: NativeFile):
    """
    Write pyarrow.Tensor to pyarrow.NativeFile object its current position.

        Parameters
        ----------
        tensor : pyarrow.Tensor
        dest : pyarrow.NativeFile

        Returns
        -------
        bytes_written : int
            Total number of bytes written to the file
    """
