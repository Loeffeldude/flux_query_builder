from flux_query_builder.functions.base import FluxQueryFunction

class Add(FluxQueryFunction):
    """date.add() adds a duration to a time value and returns the resulting time value.(Required)
Duration to add.(Required)
Time to add the duration to.Location to use for the time value.Use an absolute time or a relative duration.
Durations are relative to now().A time may be represented as either an explicit timestamp
or as a relative time from the current now time. add can
support either type of value.

    Params:
        
        d 
        - (Required)
Duration to add.
        
        to 
        - (Required)
Time to add the duration to.
        
        location 
        - Location to use for the time value.Use an absolute time or a relative duration.
Durations are relative to now().
        
    """
    name = "add"
    package="date"

    def __init__(self, d, to, location=None, ):
            super().__init__(d=d, to=to, location=location, )