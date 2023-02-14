from flux_query_builder.functions.base import FluxQueryFunction

class PromHistogramQuantile(FluxQueryFunction):
    """promql.promHistogramQuantile() implements functionality equivalent to
PromQL’s histogram_quantile() function.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).Quantile to compute ([0.0 - 1.0]).Count column name.Upper bound column name.Output value column name.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        quantile 
        - Quantile to compute ([0.0 - 1.0]).
        
        countColumn 
        - Count column name.
        
        upperBoundColumn 
        - Upper bound column name.
        
        valueColumn 
        - Output value column name.
        
    """
    name = "promHistogramQuantile"
    package="promql"

    def __init__(self, tables=None, quantile=None, countColumn=None, upperBoundColumn=None, valueColumn=None, ):
            super().__init__(tables=tables, quantile=quantile, countColumn=countColumn, upperBoundColumn=upperBoundColumn, valueColumn=valueColumn, )