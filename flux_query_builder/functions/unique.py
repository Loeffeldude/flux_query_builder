from flux_query_builder.functions.base import FluxQueryFunction

class Unique(FluxQueryFunction):
    """unique() returns all records containing unique values in a specified column.Group keys, columns, and values are not modified.
unique() drops empty tables.Column to search for unique values. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to search for unique values. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "unique"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )