from flux_query_builder.functions.base import FluxQueryFunction

class Spread(FluxQueryFunction):
    """spread() returns the difference between the minimum and maximum values in a
specified column.Column to operate on. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "spread"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )