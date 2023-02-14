from flux_query_builder.functions.base import FluxQueryFunction

class ToLower(FluxQueryFunction):
    """strings.toLower() converts a string to lowercase.(Required)
String value to convert.

    Params:
        
        v 
        - (Required)
String value to convert.
        
    """
    name = "toLower"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )