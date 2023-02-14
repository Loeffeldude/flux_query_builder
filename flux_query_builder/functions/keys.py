from flux_query_builder.functions.base import FluxQueryFunction

class Keys(FluxQueryFunction):
    """keys() returns the columns that are in the group key of each input table.Each output table contains a row for each group key column label.
A single group key column label is stored in the specified column for each row.
All columns not in the group key are dropped.Column to store group key labels in. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to store group key labels in. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "keys"
    package=None

    def __init__(self, column=None, tables=None, ):
            super().__init__(column=column, tables=tables, )