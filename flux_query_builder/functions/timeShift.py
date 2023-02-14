from flux_query_builder.functions.base import FluxQueryFunction

class TimeShift(FluxQueryFunction):
    """timeShift() adds a fixed duration to time columns.The output table schema is the same as the input table schema.
null time values remain null.(Required)
Amount of time to add to each time value. May be a negative duration.List of time columns to operate on. Default is ["_start", "_stop", "_time"].Input data. Default is piped-forward data (<-).

    Params:
        
        duration 
        - (Required)
Amount of time to add to each time value. May be a negative duration.
        
        columns 
        - List of time columns to operate on. Default is ["_start", "_stop", "_time"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "timeShift"
    package=None

    def __init__(self, duration, columns=None, tables=None, ):
            super().__init__(duration=duration, columns=columns, tables=tables, )