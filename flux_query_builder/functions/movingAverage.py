from flux_query_builder.functions.base import FluxQueryFunction

class MovingAverage(FluxQueryFunction):
    """movingAverage() calculates the mean of non-null values using the current value
and n - 1 previous values in the _values column.(Required)
Number of values to average.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of values to average.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "movingAverage"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )