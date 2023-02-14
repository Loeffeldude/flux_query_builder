from flux_query_builder.functions.base import FluxQueryFunction

class Erfc(FluxQueryFunction):
    """math.erfc() returns the complementary error function of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "erfc"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )