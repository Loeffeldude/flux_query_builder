from flux_query_builder.functions.base import FluxQueryFunction

class Trim(FluxQueryFunction):
    """strings.trim() removes leading and trailing characters specified in the cutset from a string.(Required)
String to remove characters from.(Required)
Leading and trailing characters to remove from the string.Only characters that match the cutset string exactly are trimmed.

    Params:
        
        v 
        - (Required)
String to remove characters from.
        
        cutset 
        - (Required)
Leading and trailing characters to remove from the string.Only characters that match the cutset string exactly are trimmed.
        
    """
    name = "trim"
    package="strings"

    def __init__(self, v, cutset, ):
            super().__init__(v=v, cutset=cutset, )