from flux_query_builder.functions.base import FluxQueryFunction

class Mod(FluxQueryFunction):
    """math.mod() returns a floating-point remainder of x/y.The magnitude of the result is less than y and its sign agrees
with that of x.Note: math.mod() performs the same operation as the modulo operator (%).
For example: 4.56 % 1.23(Required)
x-value to use in the operation.(Required)
y-value to use in the operation.

    Params:
        
        x 
        - (Required)
x-value to use in the operation.
        
        y 
        - (Required)
y-value to use in the operation.
        
    """
    name = "mod"
    package="math"

    def __init__(self, x, y, ):
            super().__init__(x=x, y=y, )