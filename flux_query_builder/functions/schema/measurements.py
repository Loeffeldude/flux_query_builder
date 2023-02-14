from flux_query_builder.functions.base import FluxQueryFunction

class Measurements(FluxQueryFunction):
    """schema.measurements() returns a list of measurements in a specific bucket.Results include a single table with a single column, _value.(Required)
Bucket to retrieve measurements from.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().

    Params:
        
        bucket 
        - (Required)
Bucket to retrieve measurements from.
        
        start 
        - Oldest time to include in results. Default is -30d.
        
        stop 
        - Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().
        
    """
    name = "measurements"
    package="schema"

    def __init__(self, bucket, start=None, stop=None, ):
            super().__init__(bucket=bucket, start=start, stop=stop, )