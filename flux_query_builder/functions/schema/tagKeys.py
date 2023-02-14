from flux_query_builder.functions.base import FluxQueryFunction

class TagKeys(FluxQueryFunction):
    """schema.tagKeys() returns a list of tag keys for all series that match the predicate.Results include a single table with a single column, _value.(Required)
Bucket to return tag keys from.Predicate function that filters tag keys.
Default is (r) => true.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.

    Params:
        
        bucket 
        - (Required)
Bucket to return tag keys from.
        
        predicate 
        - Predicate function that filters tag keys.
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
    name = "tagKeys"
    package="schema"

    def __init__(self, bucket, predicate=None, start=None, stop=None, ):
            super().__init__(bucket=bucket, predicate=predicate, start=start, stop=stop, )