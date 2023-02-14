from flux_query_builder.functions.base import FluxQueryFunction

class SplitAfter(FluxQueryFunction):
    """strings.splitAfter() splits a string after a specified separator and returns an array of substrings.
Split substrings include the separator, t.(Required)
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
    name = "splitAfter"
    package="strings"

    def __init__(self, v, t, ):
            super().__init__(v=v, t=t, )