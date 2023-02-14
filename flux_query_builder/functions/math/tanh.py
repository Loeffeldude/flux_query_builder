from flux_query_builder.functions.base import FluxQueryFunction

class Tanh(FluxQueryFunction):
    """math.tanh() returns the hyperbolic tangent of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "tanh"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )