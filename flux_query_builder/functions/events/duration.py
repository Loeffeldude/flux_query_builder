from flux_query_builder.functions.base import FluxQueryFunction

class Duration(FluxQueryFunction):
    """events.duration() calculates the duration of events.The function determines the time between a record and the subsequent record
and associates the duration with the first record (start of the event).
To calculate the duration of the last event,
the function compares the timestamp of the final record
to the timestamp in the stopColumn or the specified stop time.events.duration() is similar to elapsed() and stateDuration(), but differs in important ways:See the example below.Duration unit of the calculated state duration.
Default is 1ns.Name of the result column.
Default is "duration".Name of the time column.
Default is "_time".Name of the stop column.
Default is "_stop".The latest time to use when calculating results.If provided, stop overrides the time value in the stopColumn.Input data. Default is piped-forward data (<-).The example below includes output values of
events.duration(), elapsed(), and stateDuration()
related to the _time and state values of input data.

    Params:
        
        unit 
        - Duration unit of the calculated state duration.
Default is 1ns.
        
        columnName 
        - Name of the result column.
Default is "duration".
        
        timeColumn 
        - Name of the time column.
Default is "_time".
        
        stopColumn 
        - Name of the stop column.
Default is "_stop".
        
        stop 
        - The latest time to use when calculating results.If provided, stop overrides the time value in the stopColumn.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "duration"
    package="events"

    def __init__(self, unit=None, columnName=None, timeColumn=None, stopColumn=None, stop=None, tables=None, ):
            super().__init__(unit=unit, columnName=columnName, timeColumn=timeColumn, stopColumn=stopColumn, stop=stop, tables=tables, )