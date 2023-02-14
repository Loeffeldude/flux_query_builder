from flux_query_builder.functions.base import FluxQueryFunction

class Repeat(FluxQueryFunction):
    """strings.repeat() returns a string consisting of i copies of a specified string.(Required)
String value to repeat.(Required)
Number of times to repeat v.

    Params:
        
        v 
        - (Required)
String value to repeat.
        
        i 
        - (Required)
Number of times to repeat v.
        
    """
    name = "repeat"
    package="strings"

    def __init__(self, v, i, ):
            super().__init__(v=v, i=i, )