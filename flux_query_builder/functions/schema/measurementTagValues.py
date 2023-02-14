from flux_query_builder.functions.base import FluxQueryFunction

class MeasurementTagValues(FluxQueryFunction):
    """schema.measurementTagValues() returns a list of tag values for a specific measurement.Results include a single table with a single column, _value.(Required)
Bucket to return tag values from for a specific measurement.(Required)
Measurement to return tag values from.(Required)
Tag to return all unique values from.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().

    Params:
        
        bucket 
        - (Required)
Bucket to return tag values from for a specific measurement.
        
        measurement 
        - (Required)
Measurement to return tag values from.
        
        tag 
        - (Required)
Tag to return all unique values from.
        
        start 
        - Oldest time to include in results. Default is -30d.
        
        stop 
        - Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().
        
    """
    name = "measurementTagValues"
    package="schema"

    def __init__(self, bucket, measurement, tag, start=None, stop=None, ):
            super().__init__(bucket=bucket, measurement=measurement, tag=tag, start=start, stop=stop, )