from flux_query_builder.functions.base import FluxQueryFunction

class Max(FluxQueryFunction):
    """max() returns the row with the maximum value in a specified column from each
input table.Note: max() drops empty tables.Column to return maximum values from. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to return maximum values from. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "max"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )