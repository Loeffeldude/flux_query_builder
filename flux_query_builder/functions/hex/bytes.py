from flux_query_builder.functions.base import FluxQueryFunction

class Bytes(FluxQueryFunction):
    """hex.bytes() converts a hexadecimal string to bytes.(Required)
String to convert.

    Params:
        
        v 
        - (Required)
String to convert.
        
    """
    name = "bytes"
    package="hex"

    def __init__(self, v, ):
            super().__init__(v=v, )