from flux_query_builder.functions.base import FluxQueryFunction

class Mean(FluxQueryFunction):
    """experimental.mean() computes the mean or average of non-null values in the _value column
of each input table.Output tables contain a single row the with the calculated mean in the _value column.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "mean"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )