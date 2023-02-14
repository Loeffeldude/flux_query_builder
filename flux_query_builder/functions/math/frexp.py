from flux_query_builder.functions.base import FluxQueryFunction

class Frexp(FluxQueryFunction):
    """math.frexp() breaks f into a normalized fraction and an integral part of two.It returns frac and exp satisfying f == frac x 2**exp,
with the absolute value of frac in the interval [1/2, 1).(Required)
Value to operate on.

    Params:
        
        f 
        - (Required)
Value to operate on.
        
    """
    name = "frexp"
    package="math"

    def __init__(self, f, ):
            super().__init__(f=f, )