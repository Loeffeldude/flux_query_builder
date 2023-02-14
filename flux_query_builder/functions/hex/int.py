from flux_query_builder.functions.base import FluxQueryFunction

class Int(FluxQueryFunction):
    """hex.int() converts a hexadecimal string to an integer.(Required)
String to convert.

    Params:
        
        v 
        - (Required)
String to convert.
        
    """
    name = "int"
    package="hex"

    def __init__(self, v, ):
            super().__init__(v=v, )