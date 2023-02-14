from flux_query_builder.functions.base import FluxQueryFunction

class Strlen(FluxQueryFunction):
    """strings.strlen() returns the length of a string. String length is determined by the number of UTF code points a string contains.(Required)
String value to measure.

    Params:
        
        v 
        - (Required)
String value to measure.
        
    """
    name = "strlen"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )