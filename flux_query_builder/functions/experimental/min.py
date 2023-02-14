from flux_query_builder.functions.base import FluxQueryFunction

class Min(FluxQueryFunction):
    """experimental.min() returns the record with the lowest value in the _value column for each
input table.experimental.min() drops empty tables.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "min"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )