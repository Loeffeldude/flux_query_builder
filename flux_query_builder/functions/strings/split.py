from flux_query_builder.functions.base import FluxQueryFunction

class Split(FluxQueryFunction):
    """strings.split() splits a string on a specified separator and returns an array of substrings.(Required)
String value to split.(Required)
String value that acts as the separator.

    Params:
        
        v 
        - (Required)
String value to split.
        
        t 
        - (Required)
String value that acts as the separator.
        
    """
    name = "split"
    package="strings"

    def __init__(self, v, t, ):
            super().__init__(v=v, t=t, )