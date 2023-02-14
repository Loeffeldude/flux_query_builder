from flux_query_builder.functions.base import FluxQueryFunction

class Window(FluxQueryFunction):
    """window() groups records using regular time intervals.The function calculates time windows and stores window bounds in the
_start and _stop columns. _start and _stop values are assigned to
rows based on the row’s _time value.A single input row may be placed into zero or more output tables depending on
the parameters passed into window().This function is intended to be used when timeColumn (_time by default) is not in the group key.
If timeColumn is in the group key, resulting output is confusing and generally not useful.every, period, and offset parameters support all valid duration units,
including calendar months (1mo) and years (1y).When windowing by week (1w), weeks are determined using the Unix epoch
(1970-01-01T00:00:00Z UTC). The Unix epoch was on a Thursday, so all
calculated weeks begin on Thursday.Duration of time between windows.Duration of windows. Default is the every value.period can be negative, indicating the start and stop boundaries are reversed.Duration to shift the window boundaries by. Defualt is 0s.offset can be negative, indicating that the offset goes backwards in time.Location used to determine timezone. Default is the location option.Column that contains time values. Default is _time.Column to store the window start time in. Default is _start.Column to store the window stop time in. Default is _stop.Create empty tables for empty window. Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        every 
        - Duration of time between windows.
        
        period 
        - Duration of windows. Default is the every value.period can be negative, indicating the start and stop boundaries are reversed.
        
        offset 
        - Duration to shift the window boundaries by. Defualt is 0s.offset can be negative, indicating that the offset goes backwards in time.
        
        location 
        - Location used to determine timezone. Default is the location option.
        
        timeColumn 
        - Column that contains time values. Default is _time.
        
        startColumn 
        - Column to store the window start time in. Default is _start.
        
        stopColumn 
        - Column to store the window stop time in. Default is _stop.
        
        createEmpty 
        - Create empty tables for empty window. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "window"
    package=None

    def __init__(self, every=None, period=None, offset=None, location=None, timeColumn=None, startColumn=None, stopColumn=None, createEmpty=None, tables=None, ):
            super().__init__(every=every, period=period, offset=offset, location=location, timeColumn=timeColumn, startColumn=startColumn, stopColumn=stopColumn, createEmpty=createEmpty, tables=tables, )