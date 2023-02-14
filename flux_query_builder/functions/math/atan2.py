from flux_query_builder.functions.base import FluxQueryFunction

class Atan2(FluxQueryFunction):
    """math.atan2() returns the artangent of x/y, using the signs
of the two to determine the quadrant of the return value.(Required)
y-coordinate to use in the operation.(Required)
x-corrdinate to use in the operation.

    Params:
        
        y 
        - (Required)
y-coordinate to use in the operation.
        
        x 
        - (Required)
x-corrdinate to use in the operation.
        
    """
    name = "atan2"
    package="math"

    def __init__(self, y, x, ):
            super().__init__(y=y, x=x, )