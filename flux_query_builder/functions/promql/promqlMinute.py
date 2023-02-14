from flux_query_builder.functions.base import FluxQueryFunction

class PromqlMinute(FluxQueryFunction):
    """promql.promqlMinute() implements functionality equivalent to
PromQL’s minute() function.Important: The internal/promql package is not meant for external use.(Required)
Time as a floating point value.

    Params:
        
        timestamp 
        - (Required)
Time as a floating point value.
        
    """
    name = "promqlMinute"
    package="promql"

    def __init__(self, timestamp, ):
            super().__init__(timestamp=timestamp, )