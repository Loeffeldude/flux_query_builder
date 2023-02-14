from typing import Union
import inspect


class FluxQueryFunctionMeta:
    def __str__(self) -> str:
        pass


def is_flux_function(obj) -> bool:
    return inspect.isclass(obj) and issubclass(obj, FluxQueryFunction)


class FluxQueryFunction:
    params: dict
    name: str
    package: Union[str, None]

    def __init__(self, *args, **kwargs) -> None:
        self.params = kwargs

    def __str__(self) -> str:
        package_prefix = f"{self.package}." if self.package else ""
        param_strs = []

        for key, value in self.params.items():
            key: str
            if value is None:
                continue
            if key.endswith("_"):
                key = key[:-1]

            if is_flux_function(value):
                value = value.name

            param_strs.append(f"{key}: {value}")

        params = ", ".join(param_strs)
        return f"{package_prefix}{self.name}({params})"
