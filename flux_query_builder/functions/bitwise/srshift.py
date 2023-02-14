from flux_query_builder.functions.base import FluxQueryFunction

class Srshift(FluxQueryFunction):
    """bitwise.srshift() shifts the bits in a right by b bits.
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
    name = "srshift"
    package="bitwise"

    def __init__(self, a, b, ):
            super().__init__(a=a, b=b, )