from flux_query_builder.functions.base import FluxQueryFunction

class KaufmansER(FluxQueryFunction):
    """kaufmansER() computes the Kaufman’s Efficiency Ratio (KER) of values in the
_value column for each input table.Kaufman’s Efficiency Ratio indicator divides the absolute value of the Chande
Momentum Oscillator by 100 to return a value between 0 and 1.
Higher values represent a more efficient or trending market.(Required)
Period or number of points to use in the calculation.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Period or number of points to use in the calculation.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "kaufmansER"
    package=None

    def __init__(self, n, tables=None, ):
            super().__init__(n=n, tables=tables, )