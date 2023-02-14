from flux_query_builder.functions.base import FluxQueryFunction

class Exp2(FluxQueryFunction):
    """math.exp2() returns 2**x, the base-2 exponential of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "exp2"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )