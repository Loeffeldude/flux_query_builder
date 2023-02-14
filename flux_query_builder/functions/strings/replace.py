from flux_query_builder.functions.base import FluxQueryFunction

class Replace(FluxQueryFunction):
    """strings.replace() replaces the first i non-overlapping instances of a substring with
a specified replacement.(Required)
String value to search.(Required)
Substring value to replace.(Required)
Replacement for i instances of t.(Required)
Number of non-overlapping t matches to replace.

    Params:
        
        v 
        - (Required)
String value to search.
        
        t 
        - (Required)
Substring value to replace.
        
        u 
        - (Required)
Replacement for i instances of t.
        
        i 
        - (Required)
Number of non-overlapping t matches to replace.
        
    """
    name = "replace"
    package="strings"

    def __init__(self, v, t, u, i, ):
            super().__init__(v=v, t=t, u=u, i=i, )