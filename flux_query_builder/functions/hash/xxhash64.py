from flux_query_builder.functions.base import FluxQueryFunction

class Xxhash64(FluxQueryFunction):
    """hash.xxhash64() converts a string value to a 64-bit hexadecimal hash using the xxHash algorithm.(Required)
String to hash.

    Params:
        
        v 
        - (Required)
String to hash.
        
    """
    name = "xxhash64"
    package="hash"

    def __init__(self, v, ):
            super().__init__(v=v, )