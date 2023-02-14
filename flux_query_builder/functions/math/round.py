from flux_query_builder.functions.base import FluxQueryFunction

class Round(FluxQueryFunction):
    """math.round() returns the nearest integer, rounding half away from zero.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "round"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )