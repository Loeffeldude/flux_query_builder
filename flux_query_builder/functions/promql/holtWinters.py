from flux_query_builder.functions.base import FluxQueryFunction

class HoltWinters(FluxQueryFunction):
    """promql.holtWinters() implements functionality equivalent to
PromQL’s holt_winters() function.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).Exponential smoothing factor.Trend factor.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        smoothingFactor 
        - Exponential smoothing factor.
        
        trendFactor 
        - Trend factor.
        
    """
    name = "holtWinters"
    package="promql"

    def __init__(self, tables=None, smoothingFactor=None, trendFactor=None, ):
            super().__init__(tables=tables, smoothingFactor=smoothingFactor, trendFactor=trendFactor, )