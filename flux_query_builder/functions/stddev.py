from flux_query_builder.functions.base import FluxQueryFunction

class Stddev(FluxQueryFunction):
    """stddev() returns the standard deviation of non-null values in a specified column.Column to operate on. Default is _value.Standard deviation mode or type of standard deviation to calculate.
Default is sample.Availble modes:Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - Column to operate on. Default is _value.
        
        mode 
        - Standard deviation mode or type of standard deviation to calculate.
Default is sample.Availble modes:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stddev"
    package=None

    def __init__(self, column=None, mode=None, tables=None, ):
            super().__init__(column=column, mode=mode, tables=tables, )