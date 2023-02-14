from flux_query_builder.functions.base import FluxQueryFunction

class IsLetter(FluxQueryFunction):
    """strings.isLetter() tests if a single character string is a letter (a-z, A-Z).(Required)
Single-character string to test.

    Params:
        
        v 
        - (Required)
Single-character string to test.
        
    """
    name = "isLetter"
    package="strings"

    def __init__(self, v, ):
            super().__init__(v=v, )