from flux_query_builder.functions.base import FluxQueryFunction

class TripleExponentialDerivative(FluxQueryFunction):
    """tripleExponentialDerivative() returns the triple exponential derivative (TRIX)
values using n points.Triple exponential derivative, commonly referred to as “TRIX,”
is a momentum indicator and oscillator. A triple exponential derivative uses
the natural logarithm (log) of input data to calculate a triple exponential
moving average over the period of time. The calculation prevents cycles
shorter than the defined period from being considered by the indicator.
tripleExponentialDerivative() uses the time between n points to define
the period.Triple exponential derivative oscillates around a zero line.
A positive momentum oscillator value indicates an overbought market;
a negative value indicates an oversold market.
A positive momentum indicator value indicates increasing momentum;
a negative value indicates decreasing momentum.(Required)
Number of points to use in the calculation.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of points to use in the calculation.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "tripleExponentialDerivative"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )