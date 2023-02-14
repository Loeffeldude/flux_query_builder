from flux_query_builder.functions.base import FluxQueryFunction

class TrimRight(FluxQueryFunction):
    """strings.trimRight() removes trailing characters specified in the cutset from a string.(Required)
String to to remove characters from.(Required)
Trailing characters to trim from the string.Only characters that match the cutset string exactly are trimmed.

    Params:
        
        v 
        - (Required)
String to to remove characters from.
        
        cutset 
        - (Required)
Trailing characters to trim from the string.Only characters that match the cutset string exactly are trimmed.
        
    """
    name = "trimRight"
    package="strings"

    def __init__(self, v, cutset, ):
            super().__init__(v=v, cutset=cutset, )