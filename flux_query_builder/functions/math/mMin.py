from flux_query_builder.functions.base import FluxQueryFunction

class MMin(FluxQueryFunction):
    """math.mMin() is a function taht returns the lessser of x or y.(Required)
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
    name = "mMin"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )