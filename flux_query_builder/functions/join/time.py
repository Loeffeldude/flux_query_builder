from flux_query_builder.functions.base import FluxQueryFunction

class Time(FluxQueryFunction):
    """join.time() joins two table streams together exclusively on the _time column.This function calls join.tables() with the on parameter set to (l, r) => l._time == r._time.Left input stream. Default is piped-forward data (<-).(Required)
Right input stream.(Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.String that specifies the join method. Default is inner.Supported methods:

    Params:
        
        right 
        - (Required)
Right input stream.
        
        as_ 
        - (Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.
        
        left 
        - Left input stream. Default is piped-forward data (<-).
        
        method 
        - String that specifies the join method. Default is inner.Supported methods:
        
    """
    name = "time"
    package="join"

    def __init__(self, right, as_, left=None, method=None, ):
            super().__init__(right=right, as_=as_, left=left, method=method, )