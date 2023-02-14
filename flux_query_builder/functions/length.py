from flux_query_builder.functions.base import FluxQueryFunction

class Length(FluxQueryFunction):
    """length() returns the number of elements in an array.Array to evaluate. Default is the piped-forward array (<-).

    Params:
        
        arr 
        - Array to evaluate. Default is the piped-forward array (<-).
        
    """
    name = "length"
    package=None

    def __init__(self, arr=None, ):
            super().__init__(arr=arr, )