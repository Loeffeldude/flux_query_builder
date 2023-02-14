from flux_query_builder.functions.base import FluxQueryFunction

class Sum(FluxQueryFunction):
    """experimental.sum() returns the sum of non-null values in the _value column for each input table.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "sum"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )