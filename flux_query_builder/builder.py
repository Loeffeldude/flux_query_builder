from typing import Set, Union
from flux_query_builder.functions.base import FluxQueryFunction
from flux_query_builder.functions import From
from flux_query_builder.utility import S


class FluxQuery:
    query: str
    imports: Set[str]

    def __init__(self, src_bucket: str = None, start=None) -> None:
        self.query = ""
        self.imports = set()
        if src_bucket is not None:
            if start is None:
                raise ValueError("Start is required if src_bucket is provided")
            self.pipe(From(bucket=S(src_bucket), start=start))

    def _pipe_str(self, str) -> "FluxQuery":
        if len(self.query) <= 0:
            self.query += f"{str}\n"
        else:
            self.query += f"|> {str}\n"
        return self

    def pipe(self, func: Union[FluxQueryFunction, "FluxQuery"]) -> "FluxQuery":
        if func.package is not None:
            self.imports.add(func.package)

        return self._pipe_str(str(func))

    def pipe_query(self, other: "FluxQuery") -> "FluxQuery":
        self.imports.update(other.imports)
        other_query = other.get_query(with_imports=False)

        return self._pipe_str(other_query)

    def import_package(self, package: str) -> "FluxQuery":
        self.imports.append(package)

        return self

    def resolve_imports(self, query: str) -> str:
        imports_query = ""

        for import_ in self.imports:
            imports_query += f'import "{import_}"\n'

        return imports_query + query

    def get_query(self, with_imports=True) -> str:
        if with_imports:
            return self.resolve_imports(self.query)
        return self.query

    def to_string(self) -> str:
        self.get_query(with_imports=True)

    def consume(self) -> str:
        result = self.to_string()
        self.query = ""
        self.imports = set()
        return result

    def __or__(self, other: FluxQueryFunction) -> "FluxQuery":
        if isinstance(other, FluxQueryFunction):
            return self.pipe(other)
        if isinstance(other, self.__class__):
            return self.pipe_query(other)
        raise ValueError("Other has to be of type FluxQueryFunction or FluxQuery")

    def __str__(self) -> str:
        return self.to_string()
