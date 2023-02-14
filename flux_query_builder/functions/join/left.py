from flux_query_builder.functions.base import FluxQueryFunction

class Left(FluxQueryFunction):
    """join.left() performs a left outer join on two table streams.The function calls join.tables() with the method parameter set to "left".Left input stream. Default is piped-forward data (<-).(Required)
Right input stream.(Required)
Function that takes a left and right record (l, and r respectively), and returns a boolean.The body of the function must be a single boolean expression, consisting of one
or more equality comparisons between a property of l and a property of r,
each chained together by the and operator.(Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.In a left outer join, l is guaranteed to not be a default record, but r may be a
default record. Because r is more likely to contain null values, the output record
is built almost entirely from proprties of l, with the exception of v_right, which
we expect to sometimes be null.For more information about the behavior of outer joins, see the Outer joins
section in the join package documentation.

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
    name = "left"
    package="join"

    def __init__(self, right, on, as_, left=None, ):
            super().__init__(right=right, on=on, as_=as_, left=left, )