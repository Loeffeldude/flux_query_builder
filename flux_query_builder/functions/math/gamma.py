from flux_query_builder.functions.base import FluxQueryFunction

class Gamma(FluxQueryFunction):
    """math.gamma() returns the gamma function of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "gamma"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )