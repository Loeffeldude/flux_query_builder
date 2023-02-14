from flux_query_builder.functions.base import FluxQueryFunction

class Jn(FluxQueryFunction):
    """math.jn() returns the order-n Bessel funciton of the first kind.(Required)
Order number.(Required)
Value to operate on.

    Params:
        
        n 
        - (Required)
Order number.
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "jn"
    package="math"

    def __init__(self, n, x, ):
            super().__init__(n=n, x=x, )