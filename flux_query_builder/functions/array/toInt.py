from flux_query_builder.functions.base import FluxQueryFunction

class ToInt(FluxQueryFunction):
    """array.toInt() converts all values in an array to integers.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toInt"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )