from flux_query_builder.functions.base import FluxQueryFunction

class Uxor(FluxQueryFunction):
    """bitwise.uxor() performs the bitwise operation, a XOR b, with unsigned integers.(Required)
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
    name = "uxor"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )