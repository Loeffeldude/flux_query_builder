from flux_query_builder.functions.base import FluxQueryFunction

class Uint(FluxQueryFunction):
    """hex.uint() converts a hexadecimal string to an unsigned integer.(Required)
String to convert.

    Params:
        
        v 
        - (Required)
String to convert.
        
    """
    name = "uint"
    package="hex"

    def __init__(self, v, ):
            super().__init__(v=v, )