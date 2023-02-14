from flux_query_builder.functions.base import FluxQueryFunction

class HasSuffix(FluxQueryFunction):
    """strings.hasSuffix() indicates if a string ends with a specified suffix.(Required)
String value to search.(Required)
Suffix to search for.

    Params:
        
        v 
        - (Required)
String value to search.
        
        suffix 
        - (Required)
Suffix to search for.
        
    """
    name = "hasSuffix"
    package="strings"

    def __init__(self, v, suffix, ):
            super().__init__(v=v, suffix=suffix, )