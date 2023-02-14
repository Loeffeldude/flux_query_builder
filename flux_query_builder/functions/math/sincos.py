from flux_query_builder.functions.base import FluxQueryFunction

class Sincos(FluxQueryFunction):
    """math.sincos() returns the values of math.sin(x:x) and math.cos(x:x).(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "sincos"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )