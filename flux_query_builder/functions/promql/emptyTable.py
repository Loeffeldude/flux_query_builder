from flux_query_builder.functions.base import FluxQueryFunction

class EmptyTable(FluxQueryFunction):
    """promql.emptyTable() returns an empty table, which is used as a helper function to implement
PromQL’s time() and
vector() functions.Important: The internal/promql package is not meant for external use.

    Params:
        
    """
    name = "emptyTable"
    package="promql"

    def __init__(self, ):
            super().__init__()