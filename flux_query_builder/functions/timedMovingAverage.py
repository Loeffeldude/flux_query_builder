from flux_query_builder.functions.base import FluxQueryFunction

class TimedMovingAverage(FluxQueryFunction):
    """timedMovingAverage() returns the mean of values in a defined time range at a
specified frequency.For each row in a table, timedMovingAverage() returns the average of the
current value and all row values in the previous period (duration).
It returns moving averages at a frequency defined by the every parameter.every and period parameters support all valid duration units, including
calendar months (1mo) and years (1y).When aggregating by week (1w), weeks are determined using the Unix epoch
(1970-01-01T00:00:00Z UTC). The Unix epoch was on a Thursday, so all
calculated weeks begin on Thursday.(Required)
Frequency of time window.(Required)
Length of each averaged time window.A negative duration indicates start and stop boundaries are reversed.Column to operate on. Default is _value.Input data. Default is piped-forward data (<-).

    Params:
        
        every 
        - (Required)
Frequency of time window.
        
        period 
        - (Required)
Length of each averaged time window.A negative duration indicates start and stop boundaries are reversed.
        
        column 
        - Column to operate on. Default is _value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "timedMovingAverage"
    package=None

    def __init__(self, every, period, column=None, tables=None, ):
            super().__init__(every=every, period=period, column=column, tables=tables, )