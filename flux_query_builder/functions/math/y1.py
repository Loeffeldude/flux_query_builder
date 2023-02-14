from flux_query_builder.functions.base import FluxQueryFunction

class Y1(FluxQueryFunction):
    """math.y1() returns the order-one Bessel function of the second kind.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "y1"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )