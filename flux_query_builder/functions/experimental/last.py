from flux_query_builder.functions.base import FluxQueryFunction

class Last(FluxQueryFunction):
    """experimental.last() returns the last record with a non-null value in the _value column
for each input table.experimental.last() drops empty tables.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "last"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )