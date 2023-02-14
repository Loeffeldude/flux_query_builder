from flux_query_builder.functions.base import FluxQueryFunction

class Mode(FluxQueryFunction):
    """mode() returns the non-null value or values that occur most often in a
specified column in each input table.If there are multiple modes, mode() returns all mode values in a sorted table.
If there is no mode, mode() returns null.Note: mode() drops empty tables.Column to return the mode from. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to return the mode from. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "mode"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )