from flux_query_builder.functions.base import FluxQueryFunction

class Trunc(FluxQueryFunction):
    """math.trunc() returns the integer value of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "trunc"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )