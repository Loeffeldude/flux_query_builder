from flux_query_builder.functions.base import FluxQueryFunction

class Catch(FluxQueryFunction):
    """experimental.catch() calls a function and returns any error as a string value.
If the function does not error the returned value is made into a string and returned.(Required)
Function to call.

    Params:
        
        fn 
        - (Required)
Function to call.
        
    """
    name = "catch"
    package="experimental"

    def __init__(self, fn, ):
            super().__init__(fn=fn, )