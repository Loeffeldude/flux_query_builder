from flux_query_builder.functions.base import FluxQueryFunction

class AssertEmpty(FluxQueryFunction):
    """testing.assertEmpty() tests if an input stream is empty. If not empty, the function returns an error.assertEmpty can be used to perform in-line tests in a query.Input data. Default is piped-forward data (<-).This example uses testing.diff() to output the difference between two streams of tables.
testing.assertEmpty() checks to see if the difference is empty.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "assertEmpty"
    package="testing"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )