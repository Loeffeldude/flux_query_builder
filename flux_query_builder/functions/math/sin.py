from flux_query_builder.functions.base import FluxQueryFunction

class Sin(FluxQueryFunction):
    """math.sin() returns the sine of the radian argument x.(Required)
Radian value to use in the operation.

    Params:
        
        x 
        - (Required)
Radian value to use in the operation.
        
    """
    name = "sin"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )