from flux_query_builder.functions.base import FluxQueryFunction

class J0(FluxQueryFunction):
    """math.j0() returns the order-zero Bessel function of the first kind.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "j0"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )