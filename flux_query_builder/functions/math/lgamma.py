from flux_query_builder.functions.base import FluxQueryFunction

class Lgamma(FluxQueryFunction):
    """math.lgamma() returns the natural logarithm and sign (-1 or +1) of math.gamma(x:x).(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "lgamma"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )