from flux_query_builder.functions.base import FluxQueryFunction

class Roundtoeven(FluxQueryFunction):
    """math.roundtoeven() returns the nearest integer, rounding ties to even.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "roundtoeven"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )