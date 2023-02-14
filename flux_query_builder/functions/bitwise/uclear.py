from flux_query_builder.functions.base import FluxQueryFunction

class Uclear(FluxQueryFunction):
    """bitwise.uclear() performs the bitwise operation a AND NOT b, with unsigned integers.(Required)
Left hand operand.(Required)
Bits to clear.

    Params:
        
        a 
        - (Required)
Left hand operand.
        
        b 
        - (Required)
Bits to clear.
        
    """
    name = "uclear"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )