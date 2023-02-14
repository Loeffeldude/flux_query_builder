from flux_query_builder.functions.base import FluxQueryFunction

class Mean(FluxQueryFunction):
    """mean() returns the average of non-null values in a specified column from each
input table.Column to use to compute means. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to use to compute means. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "mean"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )