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
    """A Flux Query builder. This class is immutable, and all methods return a new instance of FluxQuery.
    FluxQueryFunction are added to the query by calling the method with the same name as the function.These methods are
    dynamically generated based on the functions in the functions package.

    Flux functions can also be added by calling the pipe method with a FluxQueryFunction instance.
    Or using the `|` operator.

    Example:
        >>> from flux_query_builder.builder import FluxQuery
        >>> from flux_query_builder.utility import S
        >>> import flux_query_builder.functions as fn
        
        >>> q = FluxQuery()
        >>> q = q.from_bucket("test", start="2021-01-01T00:00:00Z")
        >>> q = q.count()
        >>> q = q.rate(every="1m")
        >>> q.get_query()

        Output:
        
        ```
        import "aggregate"
        from(bucket: "test", start: "2021-01-01T00:00:00Z")
        |> count()
        |> aggregate.rate(every: "1m")
        ```

    """
    query: str
    imports: Set[str]

    def __init__(self, src_bucket: str = None, start=None) -> None:
        self.query = ""
        self.imports = set()
        if src_bucket is not None:
            if start is None:
                raise ValueError("Start is required if src_bucket is provided")
            self.pipe(From(bucket=S(src_bucket), start=start))

    def _pipe_str(self, str: str) -> "FluxQuery":
        """Private method to add a string to the query

        Args:
            str (str): the string to add to the query

        Returns:
            FluxQuery: a new instance of FluxQuery with the string added to the query
        """
        
        clone = self.clone()

        if len(self.query) <= 0:
            clone.query += f"{str}\n"
        else:
            clone.query += f"|> {str}\n"
        return clone

    def _pipe_func(self, func_class: FluxQueryFunction, *args, **kwargs) -> "FluxQuery":
        """Private method to add a FluxQueryFunction to the query

        Args:
            func_class (FluxQueryFunction):The class of the function to add to the query

        Returns:
            FluxQuery: a new instance of FluxQuery with the function added to the query
        """
        return self.pipe(func_class(*args, **kwargs))

    def clone(self) -> "FluxQuery":
        """Clone the current instance of FluxQuery

        Returns:
            FluxQuery: a new instance of FluxQuery with the same query and imports
        """
        clone = FluxQuery()
        clone.query = self.query
        clone.imports = self.imports.copy()

        return clone

    def pipe(self, func: Union[FluxQueryFunction, "FluxQuery"]) -> "FluxQuery":
        """Add a FluxQueryFunction or FluxQuery to the query

        Args:
            func (Union[FluxQueryFunction, FluxQuery]): The function or query to add to the query
            
        Returns:
            FluxQuery: a new instance of FluxQuery with the function or query added to the query
        """
        clone = self.clone()

        if func.package is not None:
            clone.imports.add(func.package)

        return clone._pipe_str(str(func))

    def pipe_query(self, other: "FluxQuery") -> "FluxQuery":
        """Adds another FluxQuery to the query

        Args:
            other (FluxQuery): The query to add to the query

        Returns:
            FluxQuery: a new instance of FluxQuery with the query added to the query
        """
        clone = self.clone()

        clone.imports.update(other.imports)
        other_query = other.get_query(with_imports=False)

        return clone._pipe_str(other_query)

    def import_package(self, package: str) -> "FluxQuery":
        """Add an import to the query

        Args:
            package (str): The package to import

        Returns:
            FluxQuery: a new instance of FluxQuery with the import added to the query
        """
        clone = self.clone()

        clone.imports.add(package)
        return clone

    def resolve_imports(self, query: str) -> str:
        """Adds the imports to the query

        Args:
            query (str): 

        Returns:
            str: _description_
        """
        imports_query = ""
        # we sort alphabetically for easier testing
        for import_ in sorted(self.imports):
            imports_query += f'import "{import_}"\n'

        return imports_query + query

    def get_query(self, with_imports=True) -> str:
        """Get the query as a string

        Args:
            with_imports (bool, optional): wether imports should be included in the resulting query. Defaults to True.

        Returns:
            str: the query as a string
        """
        if with_imports:
            return self.resolve_imports(self.query)
        return self.query

    def to_string(self) -> str:
        """Get the query as a string

        Returns:
            str: the query as a string
        """
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
