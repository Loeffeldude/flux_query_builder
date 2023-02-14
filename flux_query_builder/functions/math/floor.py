from flux_query_builder.functions.base import FluxQueryFunction

class Floor(FluxQueryFunction):
    """math.floor() returns the greatest integer value less than or equal to x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "floor"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )