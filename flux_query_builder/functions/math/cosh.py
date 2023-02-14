from flux_query_builder.functions.base import FluxQueryFunction

class Cosh(FluxQueryFunction):
    """math.cosh() returns the hyperbolic cosine of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "cosh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )