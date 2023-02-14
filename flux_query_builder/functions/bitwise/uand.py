from flux_query_builder.functions.base import FluxQueryFunction

class Uand(FluxQueryFunction):
    """bitwise.uand() performs the bitwise operation, a AND b, with unsigned integers.(Required)
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
    name = "uand"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )