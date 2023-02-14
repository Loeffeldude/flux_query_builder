from flux_query_builder.functions.base import FluxQueryFunction

class Sqrt(FluxQueryFunction):
    """math.sqrt() returns the square root of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "sqrt"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )