from flux_query_builder.functions.base import FluxQueryFunction

class ExponentialMovingAverage(FluxQueryFunction):
    """exponentialMovingAverage() calculates the exponential moving average of n
number of values in the _value column giving more weight to more recent data.(Required)
Number of values to average.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of values to average.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "exponentialMovingAverage"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )