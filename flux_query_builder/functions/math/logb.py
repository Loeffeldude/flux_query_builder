from flux_query_builder.functions.base import FluxQueryFunction

class Logb(FluxQueryFunction):
    """math.logb() returns the binary exponent of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "logb"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )