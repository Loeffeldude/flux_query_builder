from flux_query_builder.functions.base import FluxQueryFunction

class FieldKeys(FluxQueryFunction):
    """schema.fieldKeys() returns field keys in a bucket.Results include a single table with a single column, _value.Note: FieldKeys is a special application of tagValues() that returns field
keys in a given bucket.(Required)
Bucket to list field keys from.Predicate function that filters field keys.
Default is (r) => true.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.

    Params:
        
        bucket 
        - (Required)
Bucket to list field keys from.
        
        predicate 
        - Predicate function that filters field keys.
Default is (r) => true.
        
        start 
        - Oldest time to include in results. Default is -30d.
        
        stop 
        - Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.
        
    """
    name = "fieldKeys"
    package="schema"

    def __init__(self, bucket, predicate=None, start=None, stop=None, ):
            super().__init__(bucket=bucket, predicate=predicate, start=start, stop=stop, )