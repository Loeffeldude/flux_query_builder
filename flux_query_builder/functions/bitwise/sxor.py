from flux_query_builder.functions.base import FluxQueryFunction

class Sxor(FluxQueryFunction):
    """bitwise.sxor() performs the bitwise operation, a XOR b, with integers.(Required)
Left hand operand.(Required)
Right hand operand.

    Params:
        
        a 
        - (Required)
Left hand operand.
        
        b 
        - (Required)
Right hand operand.
        
    """
    name = "sxor"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )