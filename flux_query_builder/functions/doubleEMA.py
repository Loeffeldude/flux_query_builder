from flux_query_builder.functions.base import FluxQueryFunction

class DoubleEMA(FluxQueryFunction):
    """doubleEMA() returns the double exponential moving average (DEMA) of values in
the _value column grouped into n number of points, giving more weight to
recent data.(Required)
Number of points to average.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of points to average.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "doubleEMA"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )