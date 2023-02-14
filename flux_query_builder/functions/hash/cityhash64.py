from flux_query_builder.functions.base import FluxQueryFunction

class Cityhash64(FluxQueryFunction):
    """hash.cityhash64() converts a string value to a 64-bit hexadecimal hash using the CityHash64 algorithm.(Required)
String to hash.

    Params:
        
        v 
        - (Required)
String to hash.
        
    """
    name = "cityhash64"
    package="hash"

    def __init__(self, v, ):
            super().__init__(v=v, )