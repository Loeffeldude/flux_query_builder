from flux_query_builder.functions.base import FluxQueryFunction

class IsDigit(FluxQueryFunction):
    """strings.isDigit() tests if a single-character string is a digit (0-9).(Required)
Single-character string to test.

    Params:
        
        v 
        - (Required)
Single-character string to test.
        
    """
    name = "isDigit"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )