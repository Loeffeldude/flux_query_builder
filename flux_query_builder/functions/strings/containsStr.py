from flux_query_builder.functions.base import FluxQueryFunction

class ContainsStr(FluxQueryFunction):
    """strings.containsStr() reports whether a string contains a specified substring.(Required)
String value to search.(Required)
Substring value to search for.

    Params:
        
        v 
        - (Required)
String value to search.
        
        substr 
        - (Required)
Substring value to search for.
        
    """
    name = "containsStr"
    package="strings"

    def __init__(self, v, substr, ):
            super().__init__(v=v, substr=substr, )