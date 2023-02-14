from flux_query_builder.functions.base import FluxQueryFunction

class Truncate(FluxQueryFunction):
    """date.truncate() returns a time truncated to the specified duration unit.(Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().(Required)
Unit of time to truncate to.Only use 1 and the unit of time to specify the unit.
For example: 1s, 1m, 1h.Location used to determine timezone.
Default is the location option.

    Params:
        
        t 
        - (Required)
Time to operate on.Use an absolute time, relative duration, or integer.
Durations are relative to now().
        
        unit 
        - (Required)
Unit of time to truncate to.Only use 1 and the unit of time to specify the unit.
For example: 1s, 1m, 1h.
        
        location 
        - Location used to determine timezone.
Default is the location option.
        
    """
    name = "truncate"
    package="date"

    def __init__(self, t, unit, location=None, ):
            super().__init__(t=t, unit=unit, location=location, )