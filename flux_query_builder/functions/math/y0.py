from flux_query_builder.functions.base import FluxQueryFunction

class Y0(FluxQueryFunction):
    """math.y0() returns the order-zero Bessel function of the second kind.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "y0"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )