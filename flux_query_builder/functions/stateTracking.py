from flux_query_builder.functions.base import FluxQueryFunction

class StateTracking(FluxQueryFunction):
    """stateTracking() returns the cumulative count and duration of consecutive
rows that match a predicate function that defines a state.To return the cumulative count of consecutive rows that match the predicate,
include the countColumn parameter.
To return the cumulative duration of consecutive rows that match the predicate,
include the durationColumn parameter.
Rows that do not match the predicate function fn return -1 in the count
and duration columns.(Required)
Predicate function to determine state.Column to store state count in.If not defined, stateTracking() does not return the state count.Column to store state duration in.If not defined, stateTracking() does not return the state duration.Unit of time to report state duration in. Default is 1s.Column with time values used to calculate state duration.
Default is _time.Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Predicate function to determine state.
        
        countColumn 
        - Column to store state count in.If not defined, stateTracking() does not return the state count.
        
        durationColumn 
        - Column to store state duration in.If not defined, stateTracking() does not return the state duration.
        
        durationUnit 
        - Unit of time to report state duration in. Default is 1s.
        
        timeColumn 
        - Column with time values used to calculate state duration.
Default is _time.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stateTracking"
    package=None

    def __init__(self, fn, countColumn=None, durationColumn=None, durationUnit=None, timeColumn=None, tables=None, ):
            super().__init__(fn=fn, countColumn=countColumn, durationColumn=durationColumn, durationUnit=durationUnit, timeColumn=timeColumn, tables=tables, )