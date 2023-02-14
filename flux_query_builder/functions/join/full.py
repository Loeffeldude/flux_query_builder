from flux_query_builder.functions.base import FluxQueryFunction

class Full(FluxQueryFunction):
    """join.full() performs a full outer join on two table streams.The function calls join.tables() with the method parameter set to "full".Left input stream. Default is piped-forward data (<-).(Required)
Right input stream.(Required)
Function that takes a left and right record (l, and r respectively), and returns a boolean.The body of the function must be a single boolean expression, consisting of one
or more equality comparisons between a property of l and a property of r,
each chained together by the and operator.(Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.In a full outer join, either l or r could be a default record, but they will
never both be a default record at the same time.To get non-null values for the output record, check both l and r to see which contains
the desired values.The example below defines a function for the as parameter that appropriately handles
the uncertainty of a full outer join.v_left and v_right still use values from l and r directly, because we expect
them to sometimes be null in the output table.For more information about the behavior of outer joins, see the Outer joins
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
    name = "full"
    package="join"

    def __init__(self, right, on, as_, left=None, ):
            super().__init__(right=right, on=on, as_=as_, left=left, )