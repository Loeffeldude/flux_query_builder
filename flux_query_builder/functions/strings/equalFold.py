from flux_query_builder.functions.base import FluxQueryFunction

class EqualFold(FluxQueryFunction):
    """strings.equalFold() reports whether two UTF-8 strings are equal under Unicode case-folding.(Required)
String value to compare.(Required)
String value to compare against.

    Params:
        
        v 
        - (Required)
String value to compare.
        
        t 
        - (Required)
String value to compare against.
        
    """
    name = "equalFold"
    package="strings"

    def __init__(self, v, t, ):
            super().__init__(v=v, t=t, )