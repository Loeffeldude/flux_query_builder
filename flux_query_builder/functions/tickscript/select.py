from flux_query_builder.functions.base import FluxQueryFunction

class Select(FluxQueryFunction):
    """tickscript.select() changes a column’s name and optionally applies an aggregate or selector
function to values in the column.tickscript.select() is a helper function meant to replicate TICKscript operations like the following:Column to operate on. Default is _value.Aggregate or selector function to apply.(Required)
New column name.Input data. Default is piped-forward data (<-).

    Params:
        
        as_ 
        - (Required)
New column name.
        
        column 
        - Column to operate on. Default is _value.
        
        fn 
        - Aggregate or selector function to apply.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "select"
    package="tickscript"

    def __init__(self, as_, column=None, fn=None, tables=None, ):
            super().__init__(as_=as_, column=column, fn=fn, tables=tables, )