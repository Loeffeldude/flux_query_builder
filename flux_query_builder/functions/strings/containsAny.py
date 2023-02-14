from flux_query_builder.functions.base import FluxQueryFunction

class ContainsAny(FluxQueryFunction):
    """strings.containsAny() reports whether a specified string contains characters from another string.(Required)
String value to search.(Required)
Characters to search for.

    Params:
        
        v 
        - (Required)
String value to search.
        
        chars 
        - (Required)
Characters to search for.
        
    """
    name = "containsAny"
    package="strings"

    def __init__(self, v, chars, ):
            super().__init__(v=v, chars=chars, )