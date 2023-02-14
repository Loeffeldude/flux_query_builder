from flux_query_builder.functions.base import FluxQueryFunction

class TripleEMA(FluxQueryFunction):
    """tripleEMA() returns the triple exponential moving average (TEMA) of values in
the _value column.tripleEMA uses n number of points to calculate the TEMA, giving more
weight to recent data with less lag than exponentialMovingAverage() and
doubleEMA().(Required)
Number of points to use in the calculation.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of points to use in the calculation.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "tripleEMA"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )