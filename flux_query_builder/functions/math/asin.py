from flux_query_builder.functions.base import FluxQueryFunction

class Asin(FluxQueryFunction):
    """math.asin() returns the arcsine of x in radians.(Required)
Value to operate on.x should be greater than -1 and less than 1. Otherwise the function will
return NaN.

    Params:
        
        x 
        - (Required)
Value to operate on.x should be greater than -1 and less than 1. Otherwise the function will
return NaN.
        
    """
    name = "asin"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )