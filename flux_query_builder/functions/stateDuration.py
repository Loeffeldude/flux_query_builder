from flux_query_builder.functions.base import FluxQueryFunction

class StateDuration(FluxQueryFunction):
    """stateDuration() returns the cumulative duration of a given state.The state is defined by the fn predicate function. For each consecutive
record that evaluates to true, the state duration is incremented by the
duration of time between records using the specified unit. When a record
evaluates to false, the value is set to -1 and the state duration is reset.
If the record generates an error during evaluation, the point is discarded,
and does not affect the state duration.The state duration is added as an additional column to each record.
The duration is represented as an integer in the units specified.Note: As the first point in the given state has no previous point, its
state duration will be 0.(Required)
Predicate function that identifies the state of a record.Column to store the state duration in. Default is stateDuration.Time column to use to calculate elapsed time between rows.
Default is _time.Unit of time to use to increment state duration. Default is 1s (seconds).Example units:Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Predicate function that identifies the state of a record.
        
        column 
        - Column to store the state duration in. Default is stateDuration.
        
        timeColumn 
        - Time column to use to calculate elapsed time between rows.
Default is _time.
        
        unit 
        - Unit of time to use to increment state duration. Default is 1s (seconds).Example units:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stateDuration"
    package=None

    def __init__(self, fn, column=None, timeColumn=None, unit=None, tables=None, ):
            super().__init__(fn=fn, column=column, timeColumn=timeColumn, unit=unit, tables=tables, )