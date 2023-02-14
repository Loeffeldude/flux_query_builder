from flux_query_builder.functions.base import FluxQueryFunction

class Logs(FluxQueryFunction):
    """monitor.logs() retrieves notification events stored in the notifications measurement
in the _monitoring bucket.(Required)
Earliest time to include in results.Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().(Required)
Predicate function that evaluates true or false.Records or rows (r) that evaluate to true are included in output tables.
Records that evaluate to null or false are not included in output tables.

    Params:
        
        start 
        - (Required)
Earliest time to include in results.Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        fn 
        - (Required)
Predicate function that evaluates true or false.Records or rows (r) that evaluate to true are included in output tables.
Records that evaluate to null or false are not included in output tables.
        
        stop 
        - Latest time to include in results. Default is now().Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
    """
    name = "logs"
    package="monitor"

    def __init__(self, start, fn, stop=None, ):
            super().__init__(start=start, fn=fn, stop=stop, )