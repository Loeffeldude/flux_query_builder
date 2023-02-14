from flux_query_builder.functions.base import FluxQueryFunction

class Exp(FluxQueryFunction):
    """math.exp() returns e**x, the base-e exponential of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "exp"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )