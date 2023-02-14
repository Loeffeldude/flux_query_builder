from flux_query_builder.functions.base import FluxQueryFunction

class ToTime(FluxQueryFunction):
    """array.toTime() converts all values in an array to times.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toTime"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )