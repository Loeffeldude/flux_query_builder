from flux_query_builder.functions.base import FluxQueryFunction

class ShouldError(FluxQueryFunction):
    """testing.shouldError() calls a function that catches any error and checks that the error matches the expected value.(Required)
Function to call.(Required)
Regular expression to match the expected error.

    Params:
        
        fn 
        - (Required)
Function to call.
        
        want 
        - (Required)
Regular expression to match the expected error.
        
    """
    name = "shouldError"
    package="testing"

    def __init__(self, fn, want, ):
            super().__init__(fn=fn, want=want, )