from flux_query_builder.functions.base import FluxQueryFunction

class Remainder(FluxQueryFunction):
    """math.remainder() returns the IEEE 754 floating-point remainder of x/y.(Required)
Numerator to use in the operation.(Required)
Denominator to use in the operation.

    Params:
        
        x 
        - (Required)
Numerator to use in the operation.
        
        y 
        - (Required)
Denominator to use in the operation.
        
    """
    name = "remainder"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )