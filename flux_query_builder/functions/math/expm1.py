from flux_query_builder.functions.base import FluxQueryFunction

class Expm1(FluxQueryFunction):
    """math.expm1() returns e**x - 1, the base-e exponential of x minus 1.
It is more accurate than math.exp(x:x) - 1 when x is near zero.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "expm1"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )