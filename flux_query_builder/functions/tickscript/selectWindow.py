from flux_query_builder.functions.base import FluxQueryFunction

class SelectWindow(FluxQueryFunction):
    """tickscript.selectWindow() changes a column’s name, windows rows by time, and then applies an
aggregate or selector function the specified column for each window of time.tickscript.selectWindow is a helper function meant to replicate TICKscript operations like the following:Column to operate on. Default is _value.(Required)
Aggregate or selector function to apply.(Required)
New column name.(Required)
Duration of windows.(Required)
Default fill value for null values in column.
Must be the same data type as column.Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Aggregate or selector function to apply.
        
        as_ 
        - (Required)
New column name.
        
        every 
        - (Required)
Duration of windows.
        
        defaultValue 
        - (Required)
Default fill value for null values in column.
Must be the same data type as column.
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "selectWindow"
    package="tickscript"

    def __init__(self, fn, as_, every, defaultValue, column=None, tables=None, ):
            super().__init__(fn=fn, as_=as_, every=every, defaultValue=defaultValue, column=column, tables=tables, )