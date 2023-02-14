from flux_query_builder.functions.base import FluxQueryFunction

class Dim(FluxQueryFunction):
    """math.dim() returns the maximum of x - y or 0.(Required)
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
    name = "dim"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )