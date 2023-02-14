from flux_query_builder.functions.base import FluxQueryFunction

class SplitRegexp(FluxQueryFunction):
    """regexp.splitRegexp() splits a string into substrings separated by regular expression
matches and returns an array of i substrings between matches.(Required)
Regular expression used to search v.(Required)
String value to be searched.(Required)
Maximum number of substrings to return.-1 returns all matching substrings.

    Params:
        
        r 
        - (Required)
Regular expression used to search v.
        
        v 
        - (Required)
String value to be searched.
        
        i 
        - (Required)
Maximum number of substrings to return.-1 returns all matching substrings.
        
    """
    name = "splitRegexp"
    package="regexp"

    def __init__(self, r, v, i, ):
            super().__init__(r=r, v=v, i=i, )