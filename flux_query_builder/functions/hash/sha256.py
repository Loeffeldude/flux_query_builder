from flux_query_builder.functions.base import FluxQueryFunction

class Sha256(FluxQueryFunction):
    """hash.sha256() converts a string value to a hexadecimal hash using the SHA 256 hash algorithm.(Required)
String to hash.

    Params:
        
        v 
        - (Required)
String to hash.
        
    """
    name = "sha256"
    package="hash"

    def __init__(self, v, ):
            super().__init__(v=v, )