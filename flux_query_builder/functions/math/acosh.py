from flux_query_builder.functions.base import FluxQueryFunction

class Acosh(FluxQueryFunction):
    """math.acosh() returns the inverse hyperbolic cosine of x.(Required)
Value to operate on.x should be greater than 1. If less than 1 the operation will return NaN.

    Params:
        
        x 
        - (Required)
Value to operate on.x should be greater than 1. If less than 1 the operation will return NaN.
        
    """
    name = "acosh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )