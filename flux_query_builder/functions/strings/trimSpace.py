from flux_query_builder.functions.base import FluxQueryFunction

class TrimSpace(FluxQueryFunction):
    """strings.trimSpace() removes leading and trailing spaces from a string.(Required)
String to remove spaces from.

    Params:
        
        v 
        - (Required)
String to remove spaces from.
        
    """
    name = "trimSpace"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )