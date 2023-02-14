from flux_query_builder.functions.base import FluxQueryFunction

class ToBool(FluxQueryFunction):
    """toBool() converts all values in the _value column to boolean types.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toBool"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )