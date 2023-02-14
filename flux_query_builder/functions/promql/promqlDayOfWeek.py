from flux_query_builder.functions.base import FluxQueryFunction

class PromqlDayOfWeek(FluxQueryFunction):
    """promql.promqlDayOfWeek() implements functionality equivalent to
PromQL’s day_of_week() function.Important: The internal/promql package is not meant for external use.(Required)
Time as a floating point value.

    Params:
        
        timestamp 
        - (Required)
Time as a floating point value.
        
    """
    name = "promqlDayOfWeek"
    package="promql"

    def __init__(self, timestamp, ):
            super().__init__(timestamp=timestamp, )