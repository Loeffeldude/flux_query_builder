from flux_query_builder.functions.base import FluxQueryFunction

class LogarithmicBins(FluxQueryFunction):
    """logarithmicBins() generates a list of exponentially separated float values.Use linearBins() to generate bin bounds for histogram().(Required)
First value to return in the list.(Required)
Multiplier to apply to subsequent values.(Required)
Number of values to return.Include an infinite value at the end of the list. Default is true.

    Params:
        
        start 
        - (Required)
First value to return in the list.
        
        factor 
        - (Required)
Multiplier to apply to subsequent values.
        
        count 
        - (Required)
Number of values to return.
        
        infinity 
        - Include an infinite value at the end of the list. Default is true.
        
    """
    name = "logarithmicBins"
    package=None

    def __init__(self, start, factor, count, infinity=None, ):
            super().__init__(start=start, factor=factor, count=count, infinity=infinity, )