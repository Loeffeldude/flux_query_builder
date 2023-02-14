from flux_query_builder.functions.base import FluxQueryFunction

class Rename(FluxQueryFunction):
    """rename() renames columns in a table.If a column in the group key is renamed, the column name in the group key is updated.Record that maps old column names to new column names.Function that takes the current column name (column) and returns a
new column name.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - Record that maps old column names to new column names.
        
        fn 
        - Function that takes the current column name (column) and returns a
new column name.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "rename"
    package=None

    def __init__(self, columns=None, fn=None, tables=None, ):
            super().__init__(columns=columns, fn=fn, tables=tables, )