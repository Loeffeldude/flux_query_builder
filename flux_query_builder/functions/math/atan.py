from flux_query_builder.functions.base import FluxQueryFunction

class Atan(FluxQueryFunction):
    """math.atan() returns the arctangent of x in radians.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "atan"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )