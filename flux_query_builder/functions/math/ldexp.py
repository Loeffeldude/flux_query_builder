from flux_query_builder.functions.base import FluxQueryFunction

class Ldexp(FluxQueryFunction):
    """math.ldexp() is the inverse of math.frexp(). It returns frac x 2**exp.(Required)
Fraction to use in the operation.(Required)
Exponent to use in the operation.

    Params:
        
        frac 
        - (Required)
Fraction to use in the operation.
        
        exp 
        - (Required)
Exponent to use in the operation.
        
    """
    name = "ldexp"
    package="math"

    def __init__(self, frac, exp, ):
            super().__init__(frac=frac, exp=exp, )