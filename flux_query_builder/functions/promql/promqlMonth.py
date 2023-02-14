from flux_query_builder.functions.base import FluxQueryFunction

class PromqlMonth(FluxQueryFunction):
    """promql.promqlMonth() implements functionality equivalent to
PromQL’s month() function.Important: The internal/promql package is not meant for external use.(Required)
Time as a floating point value.

    Params:
        
        timestamp 
        - (Required)
Time as a floating point value.
        
    """
    name = "promqlMonth"
    package="promql"

    def __init__(self, timestamp, ):
            super().__init__(timestamp=timestamp, )