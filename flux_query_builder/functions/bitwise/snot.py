from flux_query_builder.functions.base import FluxQueryFunction

class Snot(FluxQueryFunction):
    """bitwise.snot() inverts every bit in a, an integer.(Required)
Integer to invert.

    Params:
        
        a 
        - (Required)
Integer to invert.
        
    """
    name = "snot"
    package="bitwise"

    def __init__(self, a, ):
            super().__init__(a=a, )