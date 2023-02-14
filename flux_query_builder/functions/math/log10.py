from flux_query_builder.functions.base import FluxQueryFunction

class Log10(FluxQueryFunction):
    """math.log10() returns the decimal logarithm of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "log10"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )