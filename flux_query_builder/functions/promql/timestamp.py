from flux_query_builder.functions.base import FluxQueryFunction

class Timestamp(FluxQueryFunction):
    """promql.timestamp() implements functionality equivalent to
PromQL’s timestamp() function.Important: The internal/promql package is not meant for external use.Input data. Defaults is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Defaults is piped-forward data (<-).
        
    """
    name = "timestamp"
    package="promql"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )