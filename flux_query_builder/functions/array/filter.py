from flux_query_builder.functions.base import FluxQueryFunction

class Filter(FluxQueryFunction):
    """array.filter() iterates over an array, evaluates each element with a predicate function, and then returns
a new array with only elements that match the predicate.Array to filter. Default is the piped-forward array (<-).(Required)
Predicate function to evaluate on each element.
The element is represented by x in the predicate function.

    Params:
        
        fn 
        - (Required)
Predicate function to evaluate on each element.
The element is represented by x in the predicate function.
        
        arr 
        - Array to filter. Default is the piped-forward array (<-).
        
    """
    name = "filter"
    package="array"

    def __init__(self, fn, arr=None, ):
            super().__init__(fn=fn, arr=arr, )