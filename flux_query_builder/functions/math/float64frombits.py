from flux_query_builder.functions.base import FluxQueryFunction

class Float64frombits(FluxQueryFunction):
    """math.float64frombits() returns the floating-point number corresponding to the IEE
754 binary representation b, with the sign bit of b and the result in the
same bit position.(Required)
Value to operate on.

    Params:
        
        b 
        - (Required)
Value to operate on.
        
    """
    name = "float64frombits"
    package="math"

    def __init__(self, b, ):
            super().__init__(b=b, )