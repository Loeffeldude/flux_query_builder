from flux_query_builder.functions.base import FluxQueryFunction

class MatchRegexpString(FluxQueryFunction):
    """regexp.matchRegexpString() tests if a string contains any match to a regular expression.(Required)
Regular expression used to search v.(Required)
String value to search.

    Params:
        
        r 
        - (Required)
Regular expression used to search v.
        
        v 
        - (Required)
String value to search.
        
    """
    name = "matchRegexpString"
    package="regexp"

    def __init__(self, r, v, ):
            super().__init__(r=r, v=v, )