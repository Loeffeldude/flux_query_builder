from flux_query_builder.functions.base import FluxQueryFunction

class Deadman(FluxQueryFunction):
    """monitor.deadman() detects when a group stops reporting data.
It takes a stream of tables and reports if groups have been observed since time t.monitor.deadman() retains the most recent row from each input table and adds a dead column.
If a record appears after time t, monitor.deadman() sets dead to false.
Otherwise, dead is set to true.(Required)
Time threshold for the deadman check.Input data. Default is piped-forward data (<-).Use date.add() to return a time value relative to a specified time.

    Params:
        
        t 
        - (Required)
Time threshold for the deadman check.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "deadman"
    package="monitor"

    def __init__(self, t, tables=None, ):
            super().__init__(t=t, tables=tables, )