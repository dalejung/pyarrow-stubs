"""
This type stub file was generated by pyright.
"""

from pyarrow.util import implements

_FS_DEPR_MSG = ...
class FileSystem:
    """
    Abstract filesystem interface.
    """
    def cat(self, path):
        """
        Return contents of file as a bytes object.

        Parameters
        ----------
        path : str
            File path to read content from.

        Returns
        -------
        contents : bytes
        """
        ...
    
    def ls(self, path):
        """
        Return list of file paths.

        Parameters
        ----------
        path : str
            Directory to list contents from.
        """
        ...
    
    def delete(self, path, recursive=...):
        """
        Delete the indicated file or directory.

        Parameters
        ----------
        path : str
            Path to delete.
        recursive : bool, default False
            If True, also delete child paths for directories.
        """
        ...
    
    def disk_usage(self, path): # -> Literal[0]:
        """
        Compute bytes used by all contents under indicated path in file tree.

        Parameters
        ----------
        path : str
            Can be a file path or directory.

        Returns
        -------
        usage : int
        """
        ...
    
    def stat(self, path):
        """
        Information about a filesystem entry.

        Returns
        -------
        stat : dict
        """
        ...
    
    def rm(self, path, recursive=...):
        """
        Alias for FileSystem.delete.
        """
        ...
    
    def mv(self, path, new_path):
        """
        Alias for FileSystem.rename.
        """
        ...
    
    def rename(self, path, new_path):
        """
        Rename file, like UNIX mv command.

        Parameters
        ----------
        path : str
            Path to alter.
        new_path : str
            Path to move to.
        """
        ...
    
    def mkdir(self, path, create_parents=...):
        """
        Create a directory.

        Parameters
        ----------
        path : str
            Path to the directory.
        create_parents : bool, default True
            If the parent directories don't exists create them as well.
        """
        ...
    
    def exists(self, path):
        """
        Return True if path exists.

        Parameters
        ----------
        path : str
            Path to check.
        """
        ...
    
    def isdir(self, path):
        """
        Return True if path is a directory.

        Parameters
        ----------
        path : str
            Path to check.
        """
        ...
    
    def isfile(self, path):
        """
        Return True if path is a file.

        Parameters
        ----------
        path : str
            Path to check.
        """
        ...
    
    def read_parquet(self, path, columns=..., metadata=..., schema=..., use_threads=..., use_pandas_metadata=...):
        """
        Read Parquet data from path in file system. Can read from a single file
        or a directory of files.

        Parameters
        ----------
        path : str
            Single file path or directory
        columns : List[str], optional
            Subset of columns to read.
        metadata : pyarrow.parquet.FileMetaData
            Known metadata to validate files against.
        schema : pyarrow.parquet.Schema
            Known schema to validate files against. Alternative to metadata
            argument.
        use_threads : bool, default True
            Perform multi-threaded column reads.
        use_pandas_metadata : bool, default False
            If True and file has custom pandas schema metadata, ensure that
            index columns are also loaded.

        Returns
        -------
        table : pyarrow.Table
        """
        ...
    
    def open(self, path, mode=...):
        """
        Open file for reading or writing.
        """
        ...
    
    @property
    def pathsep(self): # -> Literal['/']:
        ...
    


class LocalFileSystem(FileSystem):
    _instance = ...
    def __init__(self) -> None:
        ...
    
    @classmethod
    def get_instance(cls): # -> LocalFileSystem:
        ...
    
    @implements(FileSystem.ls)
    def ls(self, path): # -> list[str]:
        ...
    
    @implements(FileSystem.mkdir)
    def mkdir(self, path, create_parents=...): # -> None:
        ...
    
    @implements(FileSystem.isdir)
    def isdir(self, path): # -> bool:
        ...
    
    @implements(FileSystem.isfile)
    def isfile(self, path): # -> bool:
        ...
    
    @implements(FileSystem.exists)
    def exists(self, path): # -> bool:
        ...
    
    @implements(FileSystem.open)
    def open(self, path, mode=...): # -> IO[Any]:
        """
        Open file for reading or writing.
        """
        ...
    
    @property
    def pathsep(self): # -> LiteralString:
        ...
    
    def walk(self, path): # -> Iterator[tuple[str, list[str], list[str]]]:
        """
        Directory tree generator, see os.walk.
        """
        ...
    


class DaskFileSystem(FileSystem):
    """
    Wraps s3fs Dask filesystem implementation like s3fs, gcsfs, etc.
    """
    def __init__(self, fs) -> None:
        ...
    
    @implements(FileSystem.isdir)
    def isdir(self, path):
        ...
    
    @implements(FileSystem.isfile)
    def isfile(self, path):
        ...
    
    @implements(FileSystem.delete)
    def delete(self, path, recursive=...):
        ...
    
    @implements(FileSystem.exists)
    def exists(self, path):
        ...
    
    @implements(FileSystem.mkdir)
    def mkdir(self, path, create_parents=...):
        ...
    
    @implements(FileSystem.open)
    def open(self, path, mode=...):
        """
        Open file for reading or writing.
        """
        ...
    
    def ls(self, path, detail=...):
        ...
    
    def walk(self, path):
        """
        Directory tree generator, like os.walk.
        """
        ...
    


class S3FSWrapper(DaskFileSystem):
    @implements(FileSystem.isdir)
    def isdir(self, path): # -> bool:
        ...
    
    @implements(FileSystem.isfile)
    def isfile(self, path): # -> Literal[False]:
        ...
    
    def walk(self, path, refresh=...): # -> Generator[tuple[str | Unknown, list[Unknown], list[Unknown]] | Unknown, None, None]:
        """
        Directory tree generator, like os.walk.

        Generator version of what is in s3fs, which yields a flattened list of
        files.
        """
        ...
    


def resolve_filesystem_and_path(where, filesystem=...): # -> tuple[Unknown | None, Unknown] | tuple[LocalFileSystem | Unknown, str | Unknown] | tuple[HadoopFileSystem | LocalFileSystem, str | Unknown]:
    """
    Return filesystem from path which could be an HDFS URI, a local URI,
    or a plain filesystem path.
    """
    ...

