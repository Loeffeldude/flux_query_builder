from flux_query_builder.functions.base import FluxQueryFunction

class Microsecond(FluxQueryFunction):
    """date.microsecond() returns the microseconds for a specified time.
Results range from [0-999999].(Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().

    Params:
        
        t 
        - (Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().
        
    """
    name = "microsecond"
    package="date"

    def __init__(self, t, ):
            super().__init__(t=t, )