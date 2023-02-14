from flux_query_builder.functions.base import FluxQueryFunction

class Mode(FluxQueryFunction):
    """experimental.mode() computes the mode or value that occurs most often in the _value column
in each input table.experimental.mode only considers non-null values.
If there are multiple modes, it returns all modes in a sorted table.
If there is no mode, it returns null.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "mode"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )