from flux_query_builder.functions.base import FluxQueryFunction

class ReplaceAll(FluxQueryFunction):
    """strings.replaceAll() replaces all non-overlapping instances of a substring with a specified replacement.(Required)
String value to search.(Required)
Substring to replace.(Required)
Replacement for all instances of t.

    Params:
        
        v 
        - (Required)
String value to search.
        
        t 
        - (Required)
Substring to replace.
        
        u 
        - (Required)
Replacement for all instances of t.
        
    """
    name = "replaceAll"
    package="strings"

    def __init__(self, v, t, u, ):
            super().__init__(v=v, t=t, u=u, )