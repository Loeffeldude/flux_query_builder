from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """from() retrieves data from an InfluxDB bucket between the start and stop times.This version of from is equivalent to from() |> range() in a single call.(Required)
Name of the bucket to query.InfluxDB 1.x or Enterprise: Provide an empty string ("").(Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().URL of the InfluxDB instance to query.See InfluxDB OSS URLs
or InfluxDB Cloud regions.Organization name.InfluxDB API token.

    Params:
        
        bucket 
        - (Required)
Name of the bucket to query.InfluxDB 1.x or Enterprise: Provide an empty string ("").
        
        start 
        - (Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        stop 
        - Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        host 
        - URL of the InfluxDB instance to query.See InfluxDB OSS URLs
or InfluxDB Cloud regions.
        
        org 
        - Organization name.
        
        token 
        - InfluxDB API token.
        
    """
    name = "from"
    package=None

    def __init__(self, bucket, start, stop=None, host=None, org=None, token=None, ):
            super().__init__(bucket=bucket, start=start, stop=stop, host=host, org=org, token=token, )