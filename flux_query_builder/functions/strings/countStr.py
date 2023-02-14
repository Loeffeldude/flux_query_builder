from flux_query_builder.functions.base import FluxQueryFunction

class CountStr(FluxQueryFunction):
    """strings.countStr() counts the number of non-overlapping instances of a substring appears in a string.(Required)
String value to search.(Required)
Substring to count occurences of.The function counts only non-overlapping instances of substr.

    Params:
        
        v 
        - (Required)
String value to search.
        
        substr 
        - (Required)
Substring to count occurences of.The function counts only non-overlapping instances of substr.
        
    """
    name = "countStr"
    package="strings"

    def __init__(self, v, substr, ):
            super().__init__(v=v, substr=substr, )