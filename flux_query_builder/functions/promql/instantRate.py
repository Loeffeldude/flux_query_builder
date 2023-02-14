from flux_query_builder.functions.base import FluxQueryFunction

class InstantRate(FluxQueryFunction):
    """promql.instantRate() is a helper function that calculates instant rates over
counters and is used to implement PromQL’s
irate() and
idelta() functions.Important: The internal/promql package is not meant for external use.Input data. Defaults is piped-forward data (<-).Data represents a rate.

    Params:
        
        tables 
        - Input data. Defaults is piped-forward data (<-).
        
        isRate 
        - Data represents a rate.
        
    """
    name = "instantRate"
    package="promql"

    def __init__(self, tables=None, isRate=None, ):
            super().__init__(tables=tables, isRate=isRate, )