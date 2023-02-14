from flux_query_builder.functions.base import FluxQueryFunction

class Ceil(FluxQueryFunction):
    """math.ceil() returns the least integer value greater than or equal to x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "ceil"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )