from flux_query_builder.functions.base import FluxQueryFunction

class Index(FluxQueryFunction):
    """strings.index() returns the index of the first instance of a substring in a string.
If the substring is not present, it returns -1.(Required)
String value to search.(Required)
Substring to search for.

    Params:
        
        v 
        - (Required)
String value to search.
        
        substr 
        - (Required)
Substring to search for.
        
    """
    name = "index"
    package="strings"

    def __init__(self, v, substr, ):
            super().__init__(v=v, substr=substr, )