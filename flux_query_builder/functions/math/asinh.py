from flux_query_builder.functions.base import FluxQueryFunction

class Asinh(FluxQueryFunction):
    """math.asinh() returns the inverse hyperbolic sine of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "asinh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )