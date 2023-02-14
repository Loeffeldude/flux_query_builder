from flux_query_builder.functions.base import FluxQueryFunction

class Sinh(FluxQueryFunction):
    """math.sinh() returns the hyperbolic sine of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "sinh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )