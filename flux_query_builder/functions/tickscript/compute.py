from flux_query_builder.functions.base import FluxQueryFunction

class Compute(FluxQueryFunction):
    """tickscript.compute() is an alias for tickscript.select() that changes a column’s name and
optionally applies an aggregate or selector function.(Required)
New column name.Column to operate on. Default is _value.Aggregate or selector function to apply.Input data. Default is piped-forward data (<-).

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
    name = "compute"
    package="tickscript"

    def __init__(self, as_, column=None, fn=None, tables=None, ):
            super().__init__(as_=as_, column=column, fn=fn, tables=tables, )