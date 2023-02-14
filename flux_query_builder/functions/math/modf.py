from flux_query_builder.functions.base import FluxQueryFunction

class Modf(FluxQueryFunction):
    """math.modf() returns integer and fractional floating-point numbers that sum to f.Both values have the same sign as f.(Required)
Value to operate on.

    Params:
        
        f 
        - (Required)
Value to operate on.
        
    """
    name = "modf"
    package="math"

    def __init__(self, f, ):
            super().__init__(f=f, )