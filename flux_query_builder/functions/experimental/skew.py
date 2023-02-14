from flux_query_builder.functions.base import FluxQueryFunction

class Skew(FluxQueryFunction):
    """experimental.skew() returns the skew of non-null values in the _value column for each
input table as a float.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "skew"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )