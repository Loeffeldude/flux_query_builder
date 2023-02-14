from flux_query_builder.functions.base import FluxQueryFunction

class MeasurementTagKeys(FluxQueryFunction):
    """schema.measurementTagKeys() returns the list of tag keys for a specific measurement.Results include a single table with a single column, _value.(Required)
Bucket to return tag keys from for a specific measurement.(Required)
Measurement to return tag keys from.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().

    Params:
        
        bucket 
        - (Required)
Bucket to return tag keys from for a specific measurement.
        
        measurement 
        - (Required)
Measurement to return tag keys from.
        
        start 
        - Oldest time to include in results. Default is -30d.
        
        stop 
        - Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().
        
    """
    name = "measurementTagKeys"
    package="schema"

    def __init__(self, bucket, measurement, start=None, stop=None, ):
            super().__init__(bucket=bucket, measurement=measurement, start=start, stop=stop, )