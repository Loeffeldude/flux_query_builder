from flux_query_builder.functions.base import FluxQueryFunction

class LinearBins(FluxQueryFunction):
    """linearBins() generates a list of linearly separated float values.Use linearBins() to generate bin bounds for histogram().(Required)
First value to return in the list.(Required)
Distance between subsequent values.(Required)
Number of values to return.Include an infinite value at the end of the list. Default is true.

    Params:
        
        start 
        - (Required)
First value to return in the list.
        
        width 
        - (Required)
Distance between subsequent values.
        
        count 
        - (Required)
Number of values to return.
        
        infinity 
        - Include an infinite value at the end of the list. Default is true.
        
    """
    name = "linearBins"
    package=None

    def __init__(self, start, width, count, infinity=None, ):
            super().__init__(start=start, width=width, count=count, infinity=infinity, )