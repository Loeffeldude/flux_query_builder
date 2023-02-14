from flux_query_builder.functions.base import FluxQueryFunction

class ToString(FluxQueryFunction):
    """toString() converts all values in the _value column to string types.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toString"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )