from flux_query_builder.functions.base import FluxQueryFunction

class InBucket(FluxQueryFunction):
    """query.inBucket() queries data from a specified InfluxDB bucket within given time bounds,
filters data by measurement, field, and optional predicate expressions.(Required)
InfluxDB bucket name.(Required)
InfluxDB measurement name to filter by.(Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Fields to filter by. Default is [].Predicate function that evaluates column values and returns true or false.
Default is (r) => true.Records (r) are passed to the function.
Those that evaluate to true are included in the output tables.
Records that evaluate to null or false are not included in the output tables.

    Params:
        
        bucket 
        - (Required)
InfluxDB bucket name.
        
        measurement 
        - (Required)
InfluxDB measurement name to filter by.
        
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
        
        fields 
        - Fields to filter by. Default is [].
        
        predicate 
        - Predicate function that evaluates column values and returns true or false.
Default is (r) => true.Records (r) are passed to the function.
Those that evaluate to true are included in the output tables.
Records that evaluate to null or false are not included in the output tables.
        
    """
    name = "inBucket"
    package="query"

    def __init__(self, bucket, measurement, start, stop=None, fields=None, predicate=None, ):
            super().__init__(bucket=bucket, measurement=measurement, start=start, stop=stop, fields=fields, predicate=predicate, )