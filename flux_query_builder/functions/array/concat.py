from flux_query_builder.functions.base import FluxQueryFunction

class Concat(FluxQueryFunction):
    """array.concat() appends two arrays and returns a new array.Neither input array is mutated and a new array is returned.First array. Default is the piped-forward array (<-).(Required)
Array to append to the first array.

    Params:
        
        v 
        - (Required)
Array to append to the first array.
        
        arr 
        - First array. Default is the piped-forward array (<-).
        
    """
    name = "concat"
    package="array"

    def __init__(self, v, arr=None, ):
            super().__init__(v=v, arr=arr, )