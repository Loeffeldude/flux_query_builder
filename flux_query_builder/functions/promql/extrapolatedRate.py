from flux_query_builder.functions.base import FluxQueryFunction

class ExtrapolatedRate(FluxQueryFunction):
    """promql.extrapolatedRate() is a helper function that calculates extrapolated rates over
counters and is used to implement PromQL’s
rate(),
delta(),
and increase() functions.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).Data represents a counter.Data represents a rate.

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
        isCounter 
        - Data represents a counter.
        
        isRate 
        - Data represents a rate.
        
    """
    name = "extrapolatedRate"
    package="promql"

    def __init__(self, tables=None, isCounter=None, isRate=None, ):
            super().__init__(tables=tables, isCounter=isCounter, isRate=isRate, )