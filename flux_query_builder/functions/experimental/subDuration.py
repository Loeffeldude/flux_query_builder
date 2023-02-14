from flux_query_builder.functions.base import FluxQueryFunction

class SubDuration(FluxQueryFunction):
    """experimental.subDuration() subtracts a duration from a time value and returns the resulting time value.(Required)
Time to subtract the duration from.Use an absolute time or a relative duration.
Durations are relative to now().(Required)
Duration to subtract.Location to use for the time value.A time may be represented as either an explicit timestamp
or as a relative time from the current now time. subDuration can
support either type of value.

    Params:
        
        from_ 
        - (Required)
Time to subtract the duration from.Use an absolute time or a relative duration.
Durations are relative to now().
        
        d 
        - (Required)
Duration to subtract.
        
        location 
        - Location to use for the time value.
        
    """
    name = "subDuration"
    package="experimental"

    def __init__(self, from_, d, location=None, ):
            super().__init__(from_=from_, d=d, location=location, )