from typing import Set, Union
from flux_query_builder.functions.base import FluxQueryFunction
from flux_query_builder.functions import From
from flux_query_builder.utility import S
from flux_query_builder.utility.general import is_keyword

# Because of closures, we need to make a higher order function to create the methods
def get_method_for_func(func: FluxQueryFunction):
    def method(self, *args, **kwargs):
        return self._pipe_func(func, *args, **kwargs)

    return method


class FluxQueryMeta(type):
    """This metaclass is used to create a FluxQuery class that has all the functions exposed as methods"""

    def __new__(cls, name, bases, dct):
        for func in FluxQueryFunction.__subclasses__():
            if func.name is None:
                continue
            prop_name = func.name

            if func.package is not None:
                prop_name = f"{func.package}_{prop_name}"

            if is_keyword(prop_name):
                prop_name = f"{prop_name}_"

            dct[prop_name] = get_method_for_func(func)
        return super().__new__(cls, name, bases, dct)


class FluxQuery(metaclass=FluxQueryMeta):
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
        clone = self.clone()

        if len(self.query) <= 0:
            clone.query += f"{str}\n"
        else:
            clone.query += f"|> {str}\n"
        return clone

    def _pipe_func(self, func_class: FluxQueryFunction, *args, **kwargs) -> "FluxQuery":
        return self.pipe(func_class(*args, **kwargs))

    def clone(self) -> "FluxQuery":
        clone = FluxQuery()
        clone.query = self.query
        clone.imports = self.imports.copy()

        return clone

    def pipe(self, func: Union[FluxQueryFunction, "FluxQuery"]) -> "FluxQuery":
        clone = self.clone()

        if func.package is not None:
            clone.imports.add(func.package)

        return clone._pipe_str(str(func))

    def pipe_query(self, other: "FluxQuery") -> "FluxQuery":
        clone = self.clone()

        clone.imports.update(other.imports)
        other_query = other.get_query(with_imports=False)

        return clone._pipe_str(other_query)

    def import_package(self, package: str) -> "FluxQuery":
        clone = self.clone()

        clone.imports.add(package)
        return clone

    def resolve_imports(self, query: str) -> str:
        imports_query = ""
        # we sort alphabetically for easier testing
        for import_ in sorted(self.imports):
            imports_query += f'import "{import_}"\n'

        return imports_query + query

    def get_query(self, with_imports=True) -> str:
        if with_imports:
            return self.resolve_imports(self.query)
        return self.query

    def to_string(self) -> str:
        return self.get_query(with_imports=True)

    def __or__(self, other: FluxQueryFunction) -> "FluxQuery":
        if isinstance(other, FluxQueryFunction):
            return self.pipe(other)
        if isinstance(other, self.__class__):
            return self.pipe_query(other)
        raise ValueError("Other has to be of type FluxQueryFunction or FluxQuery")

    def __str__(self) -> str:
        return self.to_string()

    def __repr__(self) -> str:
        return self.to_string()
