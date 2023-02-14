from flux_query_builder.functions.base import FluxQueryFunction

class Null(FluxQueryFunction):
    """debug.null() returns the null value with a given type.Null type.Supported types:

    Params:
        
        type 
        - Null type.Supported types:
        
    """
    name = "null"
    package="debug"

    def __init__(self, type=None, ):
            super().__init__(type=type, )