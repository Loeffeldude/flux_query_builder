from flux_query_builder.functions.base import FluxQueryFunction

class Pow10(FluxQueryFunction):
    """math.pow10() returns 10**n, the base-10 exponential of n.(Required)
Exponent value.

    Params:
        
        n 
        - (Required)
Exponent value.
        
    """
    name = "pow10"
    package="math"

    def __init__(self, n, ):
            super().__init__(n=n, )