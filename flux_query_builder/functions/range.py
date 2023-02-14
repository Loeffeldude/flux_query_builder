from flux_query_builder.functions.base import FluxQueryFunction

class Range(FluxQueryFunction):
    """range() filters rows based on time bounds.Input data must have a _time column of type time.
Rows with a null value in the _time are filtered.
range() adds a _start column with the value of start and a _stop
column with the value of stop.
_start and _stop columns are added to the group key.
Each input table’s group key value is modified to fit within the time bounds.
Tables with all rows outside the time bounds are filtered entirely.(Required)
Earliest time to include in results.Results include rows with _time values that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Results exclude rows with _time values that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Input data. Default is piped-forward data (<-).

    Params:
        
        start 
        - (Required)
Earliest time to include in results.Results include rows with _time values that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        stop 
        - Latest time to include in results. Default is now().Results exclude rows with _time values that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "range"
    package=None

    def __init__(self, start, stop=None, tables=None, ):
            super().__init__(start=start, stop=stop, tables=tables, )