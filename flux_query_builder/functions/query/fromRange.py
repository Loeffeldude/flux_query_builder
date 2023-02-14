from flux_query_builder.functions.base import FluxQueryFunction

class FromRange(FluxQueryFunction):
    """query.fromRange() returns all data from a specified bucket within given time bounds.(Required)
InfluxDB bucket name.(Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().

    Params:
        
        bucket 
        - (Required)
InfluxDB bucket name.
        
        start 
        - (Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        stop 
        - Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
    """
    name = "fromRange"
    package="query"

    def __init__(self, bucket, start, stop=None, ):
            super().__init__(bucket=bucket, start=start, stop=stop, )