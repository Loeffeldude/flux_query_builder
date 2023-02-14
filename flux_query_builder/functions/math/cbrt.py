from flux_query_builder.functions.base import FluxQueryFunction

class Cbrt(FluxQueryFunction):
    """math.cbrt() returns the cube root of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "cbrt"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )