from flux_query_builder.functions.base import FluxQueryFunction, is_flux_function


class InlineFn(FluxQueryFunction):
    package = None
    name = None

    raw_fn: str

    def __init__(self, fn: str, **kwargs) -> None:
        self.raw_fn = fn
        super().__init__(**kwargs)

    @property
    def fn(self) -> str:
        result_fn = self.raw_fn
        for key, value in self.params.items():
            result_fn = result_fn.replace(f"${key}", str(value))

        return result_fn

    def __str__(self) -> str:
        return self.fn
