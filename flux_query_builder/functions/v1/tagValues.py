from flux_query_builder.functions.base import FluxQueryFunction

class TagValues(FluxQueryFunction):
    """v1.tagValues() returns a list of unique values for a given tag.Results include a single table with a single column, _value.(Required)
Bucket to return unique tag values from.(Required)
Tag to return unique values from.Predicate function that filters tag values.
Default is (r) => true.Oldest time to include in results. Default is -30d.Newest time include in results.
The stop time is exclusive, meaning values with a time equal to stop time are excluded from the results.
Default is now().Relative start times are defined using negative durations.
Negative durations are relative to now().
Absolute start times are defined using time values.

    Params:
        
        bucket 
        - (Required)
Bucket to return unique tag values from.
        
        tag 
        - (Required)
Tag to return unique values from.
        
        predicate 
        - Predicate function that filters tag values.
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
    name = "tagValues"
    package="v1"

    def __init__(self, bucket, tag, predicate=None, start=None, stop=None, ):
            super().__init__(bucket=bucket, tag=tag, predicate=predicate, start=start, stop=stop, )