from flux_query_builder.functions.base import FluxQueryFunction

class AssertEqualValues(FluxQueryFunction):
    """testing.assertEqualValues() tests whether two values are equal.(Required)
Value to test.(Required)
Expected value to test against.

    Params:
        
        got 
        - (Required)
Value to test.
        
        want 
        - (Required)
Expected value to test against.
        
    """
    name = "assertEqualValues"
    package="testing"

    def __init__(self, got, want, ):
            super().__init__(got=got, want=want, )