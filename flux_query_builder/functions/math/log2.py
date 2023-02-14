from flux_query_builder.functions.base import FluxQueryFunction

class Log2(FluxQueryFunction):
    """math.log2() is a function returns the binary logarithm of x.(Required)
the value used in the operation.

    Params:
        
        x 
        - (Required)
the value used in the operation.
        
    """
    name = "log2"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )