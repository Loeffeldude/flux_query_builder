from flux_query_builder.functions.base import FluxQueryFunction

class JsonEncode(FluxQueryFunction):
    """dynamic.jsonEncode() converts a dynamic value into JSON bytes.(Required)
Value to encode into JSON.

    Params:
        
        v 
        - (Required)
Value to encode into JSON.
        
    """
    name = "jsonEncode"
    package="dynamic"

    def __init__(self, v, ):
            super().__init__(v=v, )