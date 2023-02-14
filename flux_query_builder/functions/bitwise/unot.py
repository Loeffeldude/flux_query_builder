from flux_query_builder.functions.base import FluxQueryFunction

class Unot(FluxQueryFunction):
    """bitwise.unot() inverts every bit in a, an unsigned integer.(Required)
Unsigned integer to invert.

    Params:
        
        a 
        - (Required)
Unsigned integer to invert.
        
    """
    name = "unot"
    package="bitwise"

    def __init__(self, a, ):
            super().__init__(a=a, )