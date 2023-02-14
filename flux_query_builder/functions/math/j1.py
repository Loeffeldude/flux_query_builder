from flux_query_builder.functions.base import FluxQueryFunction

class J1(FluxQueryFunction):
    """math.j1() is a funciton that returns the order-one Bessel function for the first kind.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "j1"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )