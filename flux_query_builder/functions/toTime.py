from flux_query_builder.functions.base import FluxQueryFunction

class ToTime(FluxQueryFunction):
    """toTime() converts all values in the _value column to time types.toTime() treats all numeric input values as nanosecond epoch timestamps.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "toTime"
    package=None

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )