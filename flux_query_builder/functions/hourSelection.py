from flux_query_builder.functions.base import FluxQueryFunction

class HourSelection(FluxQueryFunction):
    """hourSelection() filters rows by time values in a specified hour range.(Required)
First hour of the hour range (inclusive). Hours range from [0-23].(Required)
Last hour of the hour range (inclusive). Hours range from [0-23].Location used to determine timezone. Default is the location option.Column that contains the time value. Default is _time.Input data. Default is piped-forward data (<-).

    Params:
        
        start 
        - (Required)
First hour of the hour range (inclusive). Hours range from [0-23].
        
        stop 
        - (Required)
Last hour of the hour range (inclusive). Hours range from [0-23].
        
        location 
        - Location used to determine timezone. Default is the location option.
        
        timeColumn 
        - Column that contains the time value. Default is _time.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "hourSelection"
    package=None

    def __init__(self, start, stop, location=None, timeColumn=None, tables=None, ):
            super().__init__(start=start, stop=stop, location=location, timeColumn=timeColumn, tables=tables, )