from flux_query_builder.functions.base import FluxQueryFunction

class Signbit(FluxQueryFunction):
    """math.signbit() reports whether x is negative or negative zero.(Required)
Value to evaluate.

    Params:
        
        x 
        - (Required)
Value to evaluate.
        
    """
    name = "signbit"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )