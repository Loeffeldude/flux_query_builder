from flux_query_builder.functions.base import FluxQueryFunction

class Load(FluxQueryFunction):
    """testing.load() loads test data from a stream of tables.Input data. Default is piped-forward data (<-).The following test uses array.from() to create two streams of tables to
compare in the test.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "load"
    package="testing"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )