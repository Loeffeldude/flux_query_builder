from flux_query_builder.functions.base import FluxQueryFunction

class Min(FluxQueryFunction):
    """min() returns the row with the minimum value in a specified column from each
input table.Note: min() drops empty tables.Column to return minimum values from. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to return minimum values from. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "min"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )