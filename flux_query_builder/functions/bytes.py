from flux_query_builder.functions.base import FluxQueryFunction

class Bytes(FluxQueryFunction):
    """bytes() converts a string value to a bytes type.(Required)
Value to convert.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "bytes"
    package=None

    def __init__(self, v, ):
            super().__init__(v=v, )