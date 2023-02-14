from flux_query_builder.functions.base import FluxQueryFunction

class SplitN(FluxQueryFunction):
    """strings.splitN() splits a string on a specified separator and returns an array of i substrings.(Required)
String value to split.(Required)
String value that acts as the separator.(Required)
Maximum number of split substrings to return.-1 returns all matching substrings.
The last substring is the unsplit remainder.

    Params:
        
        v 
        - (Required)
String value to split.
        
        t 
        - (Required)
String value that acts as the separator.
        
        i 
        - (Required)
Maximum number of split substrings to return.-1 returns all matching substrings.
The last substring is the unsplit remainder.
        
    """
    name = "splitN"
    package="strings"

    def __init__(self, v, t, i, ):
            super().__init__(v=v, t=t, i=i, )