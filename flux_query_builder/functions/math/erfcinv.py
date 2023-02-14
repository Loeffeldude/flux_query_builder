from flux_query_builder.functions.base import FluxQueryFunction

class Erfcinv(FluxQueryFunction):
    """math.erfcinv() returns the inverse of math.erfc().(Required)
Value to operate on.x should be greater than 0 and less than 2. Otherwise the operation
will return NaN.

    Params:
        
        x 
        - (Required)
Value to operate on.x should be greater than 0 and less than 2. Otherwise the operation
will return NaN.
        
    """
    name = "erfcinv"
    package="math"

    def __init__(self, x, ):
            super().__init__(x=x, )