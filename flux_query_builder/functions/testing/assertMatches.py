from flux_query_builder.functions.base import FluxQueryFunction

class AssertMatches(FluxQueryFunction):
    """testing.assertMatches() tests whether a string matches a given regex.(Required)
Value to test.(Required)
Regex to test against.

    Params:
        
        got 
        - (Required)
Value to test.
        
        want 
        - (Required)
Regex to test against.
        
    """
    name = "assertMatches"
    package="testing"

    def __init__(self, got, want, ):
            super().__init__(got=got, want=want, )