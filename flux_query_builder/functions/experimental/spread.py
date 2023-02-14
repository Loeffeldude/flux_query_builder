from flux_query_builder.functions.base import FluxQueryFunction

class Spread(FluxQueryFunction):
    """experimental.spread() returns the difference between the minimum and maximum values in the
_value column for each input table.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "spread"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )