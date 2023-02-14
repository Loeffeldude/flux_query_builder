from flux_query_builder.functions.base import FluxQueryFunction

class Compare(FluxQueryFunction):
    """strings.compare() compares the lexicographical order of two strings.(Required)
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
    name = "compare"
    package="strings"

    def __init__(self, v, t, ):
            super().__init__(v=v, t=t, )