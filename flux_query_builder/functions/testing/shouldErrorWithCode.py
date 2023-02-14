from flux_query_builder.functions.base import FluxQueryFunction

class ShouldErrorWithCode(FluxQueryFunction):
    """testing.shouldErrorWithCode() calls a function that catches any error and checks that the error matches the expected value.(Required)
Function to call.(Required)
Regular expression to match the expected error.(Required)
Which flux error code to expect

    Params:
        
        fn 
        - (Required)
Function to call.
        
        want 
        - (Required)
Regular expression to match the expected error.
        
        code 
        - (Required)
Which flux error code to expect
        
    """
    name = "shouldErrorWithCode"
    package="testing"

    def __init__(self, fn, want, code, ):
            super().__init__(fn=fn, want=want, code=code, )