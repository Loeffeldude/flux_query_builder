from flux_query_builder.functions.base import FluxQueryFunction

class Last(FluxQueryFunction):
    """last() returns the last row with a non-null value from each input table.Note: last() drops empty tables.Column to use to verify the existence of a value.
Default is _value.If this column is null in the last record, last() returns the previous
record with a non-null value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to use to verify the existence of a value.
Default is _value.If this column is null in the last record, last() returns the previous
record with a non-null value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "last"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )