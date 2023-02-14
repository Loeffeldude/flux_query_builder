from flux_query_builder.functions.base import FluxQueryFunction

class AggregateWindow(FluxQueryFunction):
    """aggregateWindow() downsamples data by grouping data into fixed windows of time
and applying an aggregate or selector function to each window.All columns not in the group key other than the specified column are dropped
from output tables. This includes _time. aggregateWindow() uses the
timeSrc and timeDst parameters to assign a time to the aggregate value.aggregateWindow() requires _start and _stop columns in input data.
Use range() to assign _start and _stop values.This function is intended to be used when timeColumn (_time by default) is not in the group key.
If timeColumn is in the group key, resulting output is confusing and generally not useful.every, period, and offset parameters support all valid duration units,
including calendar months (1mo) and years (1y).When windowing by week (1w), weeks are determined using the Unix epoch
(1970-01-01T00:00:00Z UTC). The Unix epoch was on a Thursday, so all
calculated weeks begin on Thursday.(Required)
Duration of time between windows.Duration of windows. Default is the every value.period can be negative, indicating the start and stop boundaries are reversed.Duration to shift the window boundaries by. Defualt is 0s.offset can be negative, indicating that the offset goes backwards in time.(Required)
Aggregate or selector function to apply to each time window.Location used to determine timezone. Default is the location option.Column to operate on.Column to use as the source of the new time value for aggregate values.
Default is _stop.Column to store time values for aggregate values in.
Default is _time.Create empty tables for empty window. Default is true.Note: When using createEmpty: true, aggregate functions return empty
tables, but selector functions do not. By design, selectors drop empty tables.Input data. Default is piped-forward data (<-).To use functions that don’t provide defaults for required parameters with
aggregateWindow(), define an anonymous function with column and tables
parameters that pipes-forward tables into the aggregate or selector function
with all required parameters defined:Flux increments weeks from the Unix epoch, which was a Thursday.
Because of this, by default, all 1w windows begin on Thursday.
Use the offset parameter to shift the start of weekly windows to the
desired day of the week.

    Params:
        
        every 
        - (Required)
Duration of time between windows.
        
        fn 
        - (Required)
Aggregate or selector function to apply to each time window.
        
        period 
        - Duration of windows. Default is the every value.period can be negative, indicating the start and stop boundaries are reversed.
        
        offset 
        - Duration to shift the window boundaries by. Defualt is 0s.offset can be negative, indicating that the offset goes backwards in time.
        
        location 
        - Location used to determine timezone. Default is the location option.
        
        column 
        - Column to operate on.
        
        timeSrc 
        - Column to use as the source of the new time value for aggregate values.
Default is _stop.
        
        timeDst 
        - Column to store time values for aggregate values in.
Default is _time.
        
        createEmpty 
        - Create empty tables for empty window. Default is true.Note: When using createEmpty: true, aggregate functions return empty
tables, but selector functions do not. By design, selectors drop empty tables.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "aggregateWindow"
    package=None

    def __init__(self, every, fn, period=None, offset=None, location=None, column=None, timeSrc=None, timeDst=None, createEmpty=None, tables=None, ):
            super().__init__(every=every, fn=fn, period=period, offset=offset, location=location, column=column, timeSrc=timeSrc, timeDst=timeDst, createEmpty=createEmpty, tables=tables, )