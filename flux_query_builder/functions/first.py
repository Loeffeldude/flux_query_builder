from flux_query_builder.functions.base import FluxQueryFunction

class First(FluxQueryFunction):
    """first() returns the first non-null record from each input table.Note: first() drops empty tables.Column to operate on. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "first"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )