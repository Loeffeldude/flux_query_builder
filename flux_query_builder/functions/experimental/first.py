from flux_query_builder.functions.base import FluxQueryFunction

class First(FluxQueryFunction):
    """experimental.first() returns the first record with a non-null value in the _value column
for each input table.experimental.first() drops empty tables.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "first"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )