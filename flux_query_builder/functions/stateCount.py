from flux_query_builder.functions.base import FluxQueryFunction

class StateCount(FluxQueryFunction):
    """stateCount() returns the number of consecutive rows in a given state.The state is defined by the fn predicate function. For each consecutive
record that evaluates to true, the state count is incremented. When a record
evaluates to false, the value is set to -1 and the state count is reset.
If the record generates an error during evaluation, the point is discarded,
and does not affect the state count.
The state count is added as an additional column to each record.(Required)
Predicate function that identifies the state of a record.Column to store the state count in. Default is stateCount.Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Predicate function that identifies the state of a record.
        
        column 
        - Column to store the state count in. Default is stateCount.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stateCount"
    package=None

    def __init__(self, fn, column=None, tables=None, ):
            super().__init__(fn=fn, column=column, tables=tables, )