from flux_query_builder.functions.base import FluxQueryFunction

class Log(FluxQueryFunction):
    """math.log() returns the natural logarithm of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "log"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )