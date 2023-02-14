from flux_query_builder.functions.base import FluxQueryFunction

class MeasurementFieldKeys(FluxQueryFunction):
    """schema.measurementFieldKeys() returns a list of fields in a measurement.Results include a single table with a single column, _value.(Required)
Bucket to retrieve field keys from.(Required)
Measurement to list field keys from.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.

    Params:
        
        bucket 
        - (Required)
Bucket to retrieve field keys from.
        
        measurement 
        - (Required)
Measurement to list field keys from.
        
        start 
        - Oldest time to include in results. Default is -30d.
        
        stop 
        - Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.
        
    """
    name = "measurementFieldKeys"
    package="schema"

    def __init__(self, bucket, measurement, start=None, stop=None, ):
            super().__init__(bucket=bucket, measurement=measurement, start=start, stop=stop, )