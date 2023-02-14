from flux_query_builder.functions.base import FluxQueryFunction

class Erf(FluxQueryFunction):
    """math.erf() returns the error function of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "erf"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )