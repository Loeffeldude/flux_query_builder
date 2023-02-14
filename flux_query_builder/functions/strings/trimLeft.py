from flux_query_builder.functions.base import FluxQueryFunction

class TrimLeft(FluxQueryFunction):
    """strings.trimLeft() removes specified leading characters from a string.(Required)
String to to remove characters from.(Required)
Leading characters to trim from the string.

    Params:
        
        v 
        - (Required)
String to to remove characters from.
        
        cutset 
        - (Required)
Leading characters to trim from the string.
        
    """
    name = "trimLeft"
    package="strings"

    def __init__(self, v, cutset, ):
            super().__init__(v=v, cutset=cutset, )