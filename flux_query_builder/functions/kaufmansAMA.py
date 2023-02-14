from flux_query_builder.functions.base import FluxQueryFunction

class KaufmansAMA(FluxQueryFunction):
    """kaufmansAMA() calculates the Kaufman’s Adaptive Moving Average (KAMA) using
values in input tables.Kaufman’s Adaptive Moving Average is a trend-following indicator designed to
account for market noise or volatility.(Required)
Period or number of points to use in the calculation.Column to operate on. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Period or number of points to use in the calculation.
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "kaufmansAMA"
    package=None

    def __init__(self, n, column=None, tables=None, ):
            super().__init__(n=n, column=column, tables=tables, )