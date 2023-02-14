from flux_query_builder.functions.base import FluxQueryFunction

class Log1p(FluxQueryFunction):
    """math.log1p() returns the natural logarithm of 1 plus x.
This operation is more accurate than math.log(x: 1 + x) when x is
near zero.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "log1p"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )