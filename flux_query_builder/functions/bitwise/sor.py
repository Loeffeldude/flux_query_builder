from flux_query_builder.functions.base import FluxQueryFunction

class Sor(FluxQueryFunction):
    """bitwise.sor() performs the bitwise operation, a OR b, with integers.(Required)
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
    name = "sor"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )