from flux_query_builder.functions.base import FluxQueryFunction

class AssertEquals(FluxQueryFunction):
    """testing.assertEquals() tests whether two streams of tables are identical.If equal, the function outputs the tested data stream unchanged.
If unequal, the function returns an error.assertEquals can be used to perform in-line tests in a query.(Required)
Unique assertion name.Data to test. Default is piped-forward data (<-).(Required)
Expected data to test against.

    Params:
        
        name 
        - (Required)
Unique assertion name.
        
        want 
        - (Required)
Expected data to test against.
        
        got 
        - Data to test. Default is piped-forward data (<-).
        
    """
    name = "assertEquals"
    package="testing"

    def __init__(self, name, want, got=None, ):
            super().__init__(name=name, want=want, got=got, )