from flux_query_builder.functions.base import FluxQueryFunction

class ToUInt(FluxQueryFunction):
    """toUInt() converts all values in the _value column to unsigned integer types.toUInt() behavior depends on the _value column type:Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toUInt"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )