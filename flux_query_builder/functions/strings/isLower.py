from flux_query_builder.functions.base import FluxQueryFunction

class IsLower(FluxQueryFunction):
    """strings.isLower() tests if a single-character string is lowercase.(Required)
Single-character string value to test.

    Params:
        
        v 
        - (Required)
Single-character string value to test.
        
    """
    name = "isLower"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )