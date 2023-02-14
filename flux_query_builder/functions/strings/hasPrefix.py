from flux_query_builder.functions.base import FluxQueryFunction

class HasPrefix(FluxQueryFunction):
    """strings.hasPrefix() indicates if a string begins with a specified prefix.(Required)
String value to search.(Required)
Prefix to search for.

    Params:
        
        v 
        - (Required)
String value to search.
        
        prefix 
        - (Required)
Prefix to search for.
        
    """
    name = "hasPrefix"
    package="strings"

    def __init__(self, v, prefix, ):
            super().__init__(v=v, prefix=prefix, )