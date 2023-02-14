from flux_query_builder.functions.base import FluxQueryFunction

class Quantile(FluxQueryFunction):
    """promql.quantile() accounts checks for quantile values that are out of range, above 1.0 or
below 0.0, by either returning positive infinity or negative infinity in the _value
column respectively. q must be a float.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).(Required)
Quantile to compute ([0.0 - 1.0]).Quantile method to use.

    Params:
        
        q 
        - (Required)
Quantile to compute ([0.0 - 1.0]).
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        method 
        - Quantile method to use.
        
    """
    name = "quantile"
    package="promql"

    def __init__(self, q, tables=None, method=None, ):
            super().__init__(q=q, tables=tables, method=method, )