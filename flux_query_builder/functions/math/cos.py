from flux_query_builder.functions.base import FluxQueryFunction

class Cos(FluxQueryFunction):
    """math.cos() returns the cosine of the radian argument x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "cos"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )