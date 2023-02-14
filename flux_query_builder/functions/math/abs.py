from flux_query_builder.functions.base import FluxQueryFunction

class Abs(FluxQueryFunction):
    """math.abs() returns the absolute value of x.(Required)
Value to operate on.

    Params:
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "abs"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )