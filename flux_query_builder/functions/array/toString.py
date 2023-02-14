from flux_query_builder.functions.base import FluxQueryFunction

class ToString(FluxQueryFunction):
    """array.toString() converts all values in an array to strings.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toString"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )