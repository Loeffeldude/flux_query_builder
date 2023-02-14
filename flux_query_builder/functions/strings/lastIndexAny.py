from flux_query_builder.functions.base import FluxQueryFunction

class LastIndexAny(FluxQueryFunction):
    """strings.lastIndexAny() returns the index of the last instance of any specified
characters in a string.
If none of the specified characters are present, the function returns -1.(Required)
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
    name = "lastIndexAny"
    package="strings"

    def __init__(self, v, chars, ):
            super().__init__(v=v, chars=chars, )