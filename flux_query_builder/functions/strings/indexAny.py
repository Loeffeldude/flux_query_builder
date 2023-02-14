from flux_query_builder.functions.base import FluxQueryFunction

class IndexAny(FluxQueryFunction):
    """strings.indexAny() returns the index of the first instance of specified characters in a string.
If none of the specified characters are present, it returns -1.(Required)
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
    name = "indexAny"
    package="strings"

    def __init__(self, v, chars, ):
            super().__init__(v=v, chars=chars, )