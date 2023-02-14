from flux_query_builder.functions.base import FluxQueryFunction

class Pow(FluxQueryFunction):
    """math.pow() returns x**y, the base-x exponential of y.(Required)
Base value to operate on.(Required)
Exponent value.

    Params:
        
        x 
        - (Required)
Base value to operate on.
        
        y 
        - (Required)
Exponent value.
        
    """
    name = "pow"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )