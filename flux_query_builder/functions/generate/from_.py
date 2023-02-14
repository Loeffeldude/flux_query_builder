from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """generate.from() generates data using the provided parameter values.(Required)
Number of rows to generate.(Required)
Function used to generate values.The function takes an n parameter that represents the row index, operates
on n, and then returns an integer value. Rows use zero-based indexing.(Required)
Beginning of the time range to generate values in.(Required)
End of the time range to generate values in.

    Params:
        
        count 
        - (Required)
Number of rows to generate.
        
        fn 
        - (Required)
Function used to generate values.The function takes an n parameter that represents the row index, operates
on n, and then returns an integer value. Rows use zero-based indexing.
        
        start 
        - (Required)
Beginning of the time range to generate values in.
        
        stop 
        - (Required)
End of the time range to generate values in.
        
    """
    name = "from"
    package="generate"

    def __init__(self, count, fn, start, stop, ):
            super().__init__(count=count, fn=fn, start=start, stop=stop, )