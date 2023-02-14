from flux_query_builder.functions.base import FluxQueryFunction

class Tan(FluxQueryFunction):
    """math.tan() returns the tangent of the radian argument x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "tan"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )