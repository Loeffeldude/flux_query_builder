from flux_query_builder.functions.base import FluxQueryFunction

class Slshift(FluxQueryFunction):
    """bitwise.slshift() shifts the bits in a left by b bits.
Both a and b are integers.(Required)
Left hand operand.(Required)
Number of bits to shift.

    Params:
        
        a 
        - (Required)
Left hand operand.
        
        b 
        - (Required)
Number of bits to shift.
        
    """
    name = "slshift"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )