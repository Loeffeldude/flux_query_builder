from flux_query_builder.functions.base import FluxQueryFunction

class ReplaceAllString(FluxQueryFunction):
    """regexp.replaceAllString() replaces all reguar expression matches in a string with a
specified replacement.(Required)
Regular expression used to search v.(Required)
String value to search.(Required)
Replacement for matches to r.

    Params:
        
        r 
        - (Required)
Regular expression used to search v.
        
        v 
        - (Required)
String value to search.
        
        t 
        - (Required)
Replacement for matches to r.
        
    """
    name = "replaceAllString"
    package="regexp"

    def __init__(self, r, v, t, ):
            super().__init__(r=r, v=v, t=t, )