from flux_query_builder.functions.base import FluxQueryFunction

class StateChanges(FluxQueryFunction):
    """monitor.stateChanges() detects state changes in a stream of data with a _level column
and outputs records that change from fromLevel to toLevel.Level to detect a change from. Default is "any".Level to detect a change to. Default is "any".Input data. Default is piped-forward data (<-).

    Params:
        
        fromLevel 
        - Level to detect a change from. Default is "any".
        
        toLevel 
        - Level to detect a change to. Default is "any".
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "stateChanges"
    package="monitor"

    def __init__(self, fromLevel=None, toLevel=None, tables=None, ):
            super().__init__(fromLevel=fromLevel, toLevel=toLevel, tables=tables, )