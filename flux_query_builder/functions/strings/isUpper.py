from flux_query_builder.functions.base import FluxQueryFunction

class IsUpper(FluxQueryFunction):
    """strings.isUpper() tests if a single character string is uppercase.(Required)
Single-character string value to test.

    Params:
        
        v 
        - (Required)
Single-character string value to test.
        
    """
    name = "isUpper"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )