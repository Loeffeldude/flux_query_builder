from flux_query_builder.functions.base import FluxQueryFunction

class LastIndex(FluxQueryFunction):
    """strings.lastIndex() returns the index of the last instance of a substring in a string.
If the substring is not present, the function returns -1.(Required)
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
    name = "lastIndex"
    package="strings"

    def __init__(self, v, substr, ):
            super().__init__(v=v, substr=substr, )