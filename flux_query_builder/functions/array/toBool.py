from flux_query_builder.functions.base import FluxQueryFunction

class ToBool(FluxQueryFunction):
    """array.toBool() converts all values in an array to booleans.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toBool"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )