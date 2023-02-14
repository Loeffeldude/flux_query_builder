from flux_query_builder.functions.base import FluxQueryFunction

class KaufmansAMA(FluxQueryFunction):
    """experimental.kaufmansAMA() calculates the Kaufman’s Adaptive Moving Average (KAMA) of input
tables using the _value column in each table.Kaufman’s Adaptive Moving Average is a trend-following indicator designed to
account for market noise or volatility.(Required)
Period or number of points to use in the calculation.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Period or number of points to use in the calculation.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "kaufmansAMA"
    package="experimental"

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )