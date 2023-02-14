from flux_query_builder.functions.base import FluxQueryFunction

class Second(FluxQueryFunction):
    """date.second() returns the second of a specified time. Results range from [0 - 59].(Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().

    Params:
        
        t 
        - (Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().
        
    """
    name = "second"
    package="date"

    def __init__(self, t, ):
            super().__init__(t=t, )