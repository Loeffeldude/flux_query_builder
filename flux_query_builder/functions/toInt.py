from flux_query_builder.functions.base import FluxQueryFunction

class ToInt(FluxQueryFunction):
    """toInt() converts all values in the _value column to integer types.toInt() behavior depends on the _value column type:Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toInt"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )