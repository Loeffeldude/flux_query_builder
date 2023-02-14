from flux_query_builder.functions.base import FluxQueryFunction

class ToFloat(FluxQueryFunction):
    """toFloat() converts all values in the _value column to float types.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toFloat"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )