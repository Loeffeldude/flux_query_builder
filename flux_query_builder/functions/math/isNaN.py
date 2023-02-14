from flux_query_builder.functions.base import FluxQueryFunction

class IsNaN(FluxQueryFunction):
    """math.isNaN() reports whether f is an IEEE 754 “not-a-number” value.(Required)
Value to operate on.

    Params:
        
        f 
        - (Required)
Value to operate on.
        
    """
    name = "isNaN"
    package="math"

    def __init__(self, f, ):
            super().__init__(f=f, )