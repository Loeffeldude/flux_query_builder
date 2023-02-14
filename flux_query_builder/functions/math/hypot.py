from flux_query_builder.functions.base import FluxQueryFunction

class Hypot(FluxQueryFunction):
    """math.hypot() returns the square root of p*p + q*q, taking care to avoid overflow
and underflow.(Required)
p-value to use in the operation.(Required)
q-value to use in the operation.

    Params:
        
        p 
        - (Required)
p-value to use in the operation.
        
        q 
        - (Required)
q-value to use in the operation.
        
    """
    name = "hypot"
    package="math"

    def __init__(self, p, q, ):
            super().__init__(p=p, q=q, )