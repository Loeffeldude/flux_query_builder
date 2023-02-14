from flux_query_builder.functions.base import FluxQueryFunction

class Changes(FluxQueryFunction):
    """promql.changes() implements functionality equivalent to
PromQL’s changes() function.Important: The internal/promql package is not meant for external use.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "changes"
    package="promql"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )