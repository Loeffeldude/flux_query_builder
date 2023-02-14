from flux_query_builder.functions.base import FluxQueryFunction

class Float64bits(FluxQueryFunction):
    """math.float64bits() returns the IEEE 754 binary representation of f,
with the sign bit of f and the result in the same bit position.(Required)
Value to operate on.

    Params:
        
        f 
        - (Required)
Value to operate on.
        
    """
    name = "float64bits"
    package="math"

    def __init__(self, f, ):
            super().__init__(f=f, )