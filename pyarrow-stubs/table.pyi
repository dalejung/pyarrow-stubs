from __future__ import annotations
import pandas as pd

from typing_extensions import Self
from pyarrow_stubs_ext import PaArray
from .lib import (
    _Weakrefable as _Weakrefable,
    _PandasConvertible as _PandasConvertible
)
from .schema import Schema
from .field import Field
from .compute import CastOptions


class Table(_PandasConvertible):
    """
    Table()

        A collection of top-level named, equal length Arrow arrays.

        Warnings
        --------
        Do not call this class's constructor directly, use one of the ``from_*``
        methods instead.

        Examples
        --------
        >>> import pyarrow as pa
        >>> n_legs = pa.array([2, 4, 5, 100])
        >>> animals = pa.array(["Flamingo", "Horse", "Brittle stars", "Centipede"])
        >>> names = ["n_legs", "animals"]

        Construct a Table from arrays:

        >>> pa.Table.from_arrays([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]

        Construct a Table from a RecordBatch:

        >>> batch = pa.record_batch([n_legs, animals], names=names)
        >>> pa.Table.from_batches([batch])
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]

        Construct a Table from pandas DataFrame:

        >>> import pandas as pd
        >>> df = pd.DataFrame({'year': [2020, 2022, 2019, 2021],
        ...                    'n_legs': [2, 4, 5, 100],
        ...                    'animals': ["Flamingo", "Horse", "Brittle stars", "Centipede"]})
        >>> pa.Table.from_pandas(df)
        pyarrow.Table
        year: int64
        n_legs: int64
        animals: string
        ----
        year: [[2020,2022,2019,2021]]
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]

        Construct a Table from a dictionary of arrays:

        >>> pydict = {'n_legs': n_legs, 'animals': animals}
        >>> pa.Table.from_pydict(pydict)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
        >>> pa.Table.from_pydict(pydict).schema
        n_legs: int64
        animals: string

        Construct a Table from a dictionary of arrays with metadata:

        >>> my_metadata={"n_legs": "Number of legs per animal"}
        >>> pa.Table.from_pydict(pydict, metadata=my_metadata).schema
        n_legs: int64
        animals: string
        -- schema metadata --
        n_legs: 'Number of legs per animal'

        Construct a Table from a list of rows:

        >>> pylist = [{'n_legs': 2, 'animals': 'Flamingo'}, {'year': 2021, 'animals': 'Centipede'}]
        >>> pa.Table.from_pylist(pylist)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,null]]
        animals: [["Flamingo","Centipede"]]

        Construct a Table from a list of rows with pyarrow schema:

        >>> my_schema = pa.schema([
        ...     pa.field('year', pa.int64()),
        ...     pa.field('n_legs', pa.int64()),
        ...     pa.field('animals', pa.string())],
        ...     metadata={"year": "Year of entry"})
        >>> pa.Table.from_pylist(pylist, schema=my_schema).schema
        year: int64
        n_legs: int64
        animals: string
        -- schema metadata --
        year: 'Year of entry'

        Construct a Table with :func:`pyarrow.table`:

        >>> pa.table([n_legs, animals], names=names)
        pyarrow.Table
        n_legs: int64
        animals: string
        ----
        n_legs: [[2,4,5,100]]
        animals: [["Flamingo","Horse","Brittle stars","Centipede"]]
    """
    schema: Schema
    column_names: list[str]

    def __len__(self) -> int:
        ...

    def filter(self, mask, null_selection_behavior=...) -> Table:
        ...

    def take(self, indices) -> Table:
        ...

    def sort_by(self, sorting: str | list[tuple[str, str]]) -> Table:
        ...

    def __getitem__(self, key) -> PaArray:
        ...

    def add_column(self, i: int, field_: str | Field, column) -> Table:
        ...

    @classmethod
    def from_pandas(cls, df: pd.DataFrame, schema: Schema | None = ..., preserve_index=...,
                    nthreads=..., columns=..., safe=...) -> Table:
        ...

    def to_pylist(self) -> list[dict]:
        ...

    def drop(self, columns: list[str]) -> Self:
        ...

    def cast(self, schema: Schema, safe: bool = True,
             options: CastOptions | None = None) -> Table:
        ...

    def slice(self, offset: int = 0, length: int | None = None) -> Table:
        ...

    def group_by(self, keys: str | list[str]) -> TableGroupBy:
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
