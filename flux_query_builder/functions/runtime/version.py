from flux_query_builder.functions.base import FluxQueryFunction

class Version(FluxQueryFunction):
    """runtime.version() returns the current Flux version.

    Params:
        
    """
    name = "version"
    package="runtime"

    def __init__(self, ):
            super().__init__()