from flux_query_builder.functions.base import FluxQueryFunction

class MInf(FluxQueryFunction):
    """math.mInf() returns positive infinity if sign >= 0, negative infinity
if sign < 0.(Required)
Value to operate on.

    Params:
        
        sign 
        - (Required)
Value to operate on.
        
    """
    name = "mInf"
    package="math"

    def __init__(self, sign, ):
            super().__init__(sign=sign, )