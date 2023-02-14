from flux_query_builder.functions.base import FluxQueryFunction

class ToFloat(FluxQueryFunction):
    """array.toFloat() converts all values in an array to floats.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toFloat"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )