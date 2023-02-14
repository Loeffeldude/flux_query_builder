from flux_query_builder.functions.base import FluxQueryFunction

class Yn(FluxQueryFunction):
    """math.yn() returns the order-n Bessel function of the second kind.(Required)
Order number to use in the operation.(Required)
Value to operate on.

    Params:
        
        n 
        - (Required)
Order number to use in the operation.
        
        x 
        - (Required)
Value to operate on.
        
    """
    name = "yn"
    package="math"

    def __init__(self, n, x, ):
            super().__init__(n=n, x=x, )