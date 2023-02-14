from flux_query_builder.functions.base import FluxQueryFunction

class IsInf(FluxQueryFunction):
    """math.isInf() reports whether f is an infinity, according to sign.If sign > 0, math.isInf reports whether f is positive infinity.
If sign < 0, math.isInf reports whether f is negative infinity.
If sign == 0, math.isInf reports whether f is either infinity.(Required)
is the value used in the evaluation.(Required)
is the sign used in the eveluation.

    Params:
        
        f 
        - (Required)
is the value used in the evaluation.
        
        sign 
        - (Required)
is the sign used in the eveluation.
        
    """
    name = "isInf"
    package="math"

    def __init__(self, f, sign, ):
            super().__init__(f=f, sign=sign, )