from flux_query_builder.functions.base import FluxQueryFunction

class Unique(FluxQueryFunction):
    """experimental.unique() returns all records containing unique values in the _value column.null is considered a unique value.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "unique"
    package="experimental"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )