from flux_query_builder.functions.base import FluxQueryFunction

class StateChangesOnly(FluxQueryFunction):
    """monitor.stateChangesOnly() takes a stream of tables that contains a _level column
and returns a stream of tables grouped by _level where each record
represents a state change.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stateChangesOnly"
    package="monitor"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )