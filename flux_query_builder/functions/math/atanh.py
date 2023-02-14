from flux_query_builder.functions.base import FluxQueryFunction

class Atanh(FluxQueryFunction):
    """math.atanh() returns the inverse hyperbolic tangent of x.(Required)
Value to operate on.x should be greater than -1 and less than 1. Otherwise the operation
will return NaN.

    Params:
        
        x 
        - (Required)
Value to operate on.x should be greater than -1 and less than 1. Otherwise the operation
will return NaN.
        
    """
    name = "atanh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )