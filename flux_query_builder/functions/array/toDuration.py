from flux_query_builder.functions.base import FluxQueryFunction

class ToDuration(FluxQueryFunction):
    """array.toDuration() converts all values in an array to durations.Array of values to convert. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array of values to convert. Default is the piped-forward array (<-).
        
    """
    name = "toDuration"
    package="array"

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )