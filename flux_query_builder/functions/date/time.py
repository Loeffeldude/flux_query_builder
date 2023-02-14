from flux_query_builder.functions.base import FluxQueryFunction

class Time(FluxQueryFunction):
    """date.time() returns the time value of a specified relative duration or time.date.time assumes duration values are relative to now().(Required)
Duration or time value.Use an absolute time or relative duration.
Durations are relative to now().Location used to determine timezone.
Default is the location option.

    Params:
        
        t 
        - (Required)
Duration or time value.Use an absolute time or relative duration.
Durations are relative to now().
        
        location 
        - Location used to determine timezone.
Default is the location option.
        
    """
    name = "time"
    package="date"

    def __init__(self, t, location=None, ):
            super().__init__(t=t, location=location, )