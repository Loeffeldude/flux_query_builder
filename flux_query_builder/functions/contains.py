from flux_query_builder.functions.base import FluxQueryFunction

class Contains(FluxQueryFunction):
    """contains() tests if an array contains a specified value and returns true or false.(Required)
Value to search for.(Required)
Array to search.

    Params:
        
        value 
        - (Required)
Value to search for.
        
        set 
        - (Required)
Array to search.
        
    """
    name = "contains"
    package=None

    def __init__(self, value, set, ):
            super().__init__(value=value, set=set, )