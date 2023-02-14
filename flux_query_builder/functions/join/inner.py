from flux_query_builder.functions.base import FluxQueryFunction

class Inner(FluxQueryFunction):
    """join.inner() performs an inner join on two table streams.The function calls join.tables() with the method parameter set to "inner".Left input stream. Default is piped-forward data (<-).(Required)
Right input stream.(Required)
Function that takes a left and right record (l, and r respectively), and returns a boolean.The body of the function must be a single boolean expression, consisting of one
or more equality comparisons between a property of l and a property of r,
each chained together by the and operator.(Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.

    Params:
        
        right 
        - (Required)
Right input stream.
        
        on 
        - (Required)
Function that takes a left and right record (l, and r respectively), and returns a boolean.The body of the function must be a single boolean expression, consisting of one
or more equality comparisons between a property of l and a property of r,
each chained together by the and operator.
        
        as_ 
        - (Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.
        
        left 
        - Left input stream. Default is piped-forward data (<-).
        
    """
    name = "inner"
    package="join"

    def __init__(self, right, on, as_, left=None, ):
            super().__init__(right=right, on=on, as_=as_, left=left, )