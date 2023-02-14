from flux_query_builder.functions.base import FluxQueryFunction

class Preview(FluxQueryFunction):
    """experimental.preview() limits the number of rows and tables in the stream.Included group keys are not deterministic and depends on the order
that the engine sends them.Maximum number of rows per table to return. Default is 5.Maximum number of tables to return.
Default is 5.Input data. Default is piped-forward data (<-).

    Params:
        
        nrows 
        - Maximum number of rows per table to return. Default is 5.
        
        ntables 
        - Maximum number of tables to return.
Default is 5.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "preview"
    package="experimental"

    def __init__(self, nrows=None, ntables=None, tables=None, ):
            super().__init__(nrows=nrows, ntables=ntables, tables=tables, )