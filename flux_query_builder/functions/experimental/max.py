from flux_query_builder.functions.base import FluxQueryFunction

class Max(FluxQueryFunction):
    """experimental.max() returns the record with the highest value in the _value column for each
input table.// experimental.max() drops empty tables.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "max"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )