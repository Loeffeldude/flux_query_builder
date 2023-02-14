from flux_query_builder.functions.base import FluxQueryFunction

class Copysign(FluxQueryFunction):
    """math.copysign() returns a value with the magnitude x and the sign of y.(Required)
Magnitude to use in the operation.(Required)
Sign to use in the operation.

    Params:
        
        x 
        - (Required)
Magnitude to use in the operation.
        
        y 
        - (Required)
Sign to use in the operation.
        
    """
    name = "copysign"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )