from flux_query_builder.functions.base import FluxQueryFunction

class Sclear(FluxQueryFunction):
    """bitwise.sclear() performs the bitwise operation a AND NOT b.
Both a and b are integers.(Required)
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
    name = "sclear"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )