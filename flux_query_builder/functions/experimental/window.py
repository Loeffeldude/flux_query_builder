from flux_query_builder.functions.base import FluxQueryFunction

class Window(FluxQueryFunction):
    """experimental.window() groups records based on time._start and _stop columns are updated to reflect the bounds of
the window the row’s time value is in.
Input tables must have _start, _stop, and _time columns.A single input record can be placed into zero or more output tables depending
on the specific windowing function.By default the start boundary of a window will align with the Unix epoch
modified by the offset of the location option.every, period, and offset support all valid duration units, including
calendar months (1mo) and years (1y).Duration of time between windows. Default is the 0s.Duration of the window. Default is 0s.Period is the length of each interval.
It can be negative, indicating the start and stop boundaries are reversed.Duration to shift the window boundaries by. Default is 0s.offset can be negative, indicating that the offset goes backwards in time.Location used to determine timezone. Default is the location option.Create empty tables for empty windows. Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        every 
        - Duration of time between windows. Default is the 0s.
        
        period 
        - Duration of the window. Default is 0s.Period is the length of each interval.
It can be negative, indicating the start and stop boundaries are reversed.
        
        offset 
        - Duration to shift the window boundaries by. Default is 0s.offset can be negative, indicating that the offset goes backwards in time.
        
        location 
        - Location used to determine timezone. Default is the location option.
        
        createEmpty 
        - Create empty tables for empty windows. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "window"
    package="experimental"

    def __init__(self, every=None, period=None, offset=None, location=None, createEmpty=None, tables=None, ):
            super().__init__(every=every, period=period, offset=offset, location=location, createEmpty=createEmpty, tables=tables, )