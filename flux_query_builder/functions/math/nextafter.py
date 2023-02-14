from flux_query_builder.functions.base import FluxQueryFunction

class Nextafter(FluxQueryFunction):
    """math.nextafter() returns the next representable float value after x towards y.(Required)
x-value to use in the operation.(Required)
y-value to use in the operation.

    Params:
        
        x 
        - (Required)
x-value to use in the operation.
        
        y 
        - (Required)
y-value to use in the operation.
        
    """
    name = "nextafter"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )