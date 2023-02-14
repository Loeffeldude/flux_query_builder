from flux_query_builder.functions.base import FluxQueryFunction

class Encode(FluxQueryFunction):
    """json.encode() converts a value into JSON bytes.This function encodes Flux types as follows:(Required)
Value to convert.

    Params:
        
        v 
        - (Required)
Value to convert.
        
    """
    name = "encode"
    package="json"

    def __init__(self, v, ):
            super().__init__(v=v, )