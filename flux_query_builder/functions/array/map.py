from flux_query_builder.functions.base import FluxQueryFunction

class Map(FluxQueryFunction):
    """array.map() iterates over an array, applies a function to each element to produce a new element,
and then returns a new array.Array to operate on. Defaults is the piped-forward array (<-).(Required)
Function to apply to elements. The element is represented by x in the function.

    Params:
        
        fn 
        - (Required)
Function to apply to elements. The element is represented by x in the function.
        
        arr 
        - Array to operate on. Defaults is the piped-forward array (<-).
        
    """
    name = "map"
    package="array"

    def __init__(self, fn, arr=None, ):
            super().__init__(fn=fn, arr=arr, )