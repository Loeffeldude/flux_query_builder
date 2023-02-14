from flux_query_builder.functions.base import FluxQueryFunction

class ToUInt(FluxQueryFunction):
    """array.toUInt() converts all values in an array to unsigned integers.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toUInt"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )