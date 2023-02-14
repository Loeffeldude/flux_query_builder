from flux_query_builder.functions.base import FluxQueryFunction

class Ilogb(FluxQueryFunction):
    """math.ilogb() returns the binary exponent of x as an integer.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "ilogb"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )