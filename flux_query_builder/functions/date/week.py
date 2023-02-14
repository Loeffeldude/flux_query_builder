from flux_query_builder.functions.base import FluxQueryFunction

class Week(FluxQueryFunction):
    """date.week() returns the ISO week of the year for a specified time.
Results range from [1 - 53].(Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().Location used to determine timezone.
Default is the location option.

    Params:
        
        t 
        - (Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().
        
        location 
        - Location used to determine timezone.
Default is the location option.
        
    """
    name = "week"
    package="date"

    def __init__(self, t, location=None, ):
            super().__init__(t=t, location=location, )