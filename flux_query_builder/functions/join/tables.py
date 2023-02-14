from flux_query_builder.functions.base import FluxQueryFunction

class Tables(FluxQueryFunction):
    """join.tables() joins two input streams together using a specified method, predicate, and a function to join two corresponding records, one from each input stream.join.tables() only compares records with the same group key. Output tables have the same grouping as the input tables.Left input stream. Default is piped-forward data (<-).(Required)
Right input stream.(Required)
Function that takes a left and right record (l, and r respectively), and returns a boolean.The body of the function must be a single boolean expression, consisting of one
or more equality comparisons between a property of l and a property of r,
each chained together by the and operator.(Required)
Function that takes a left and a right record (l and r respectively), and returns a record.
The returned record is included in the final output.(Required)
String that specifies the join method.Supported methods:If the join method is anything other than inner, pay special attention to how
the output record is constructed in the as function.Because of how flux handles outer joins, it’s possible for either l or r to be a
default record. This means any value in a non-group-key column could be null.For more information about the behavior of outer joins, see the Outer joins
section in the join package documentation.In the case of a left outer join, l is guaranteed to not be a default record. To
ensure that the output record has non-null values for any columns that aren’t part
of the group key, use values from l. Using a non-group-key value from r risks
that value being null.The example below constructs the output record almost entirely from properties of l.
The only exception is the v_right column which gets its value from r._value.
In this case, understand and expect that v_right will sometimes be null.The next example is nearly identical to the previous example,
but uses the right join method. With this method, r is guaranteed to not be a default
record, but l may be a default record. Because l is more likely to contain null values,
the output record is built almost entirely from proprties of r, with the exception of
v_left, which we expect to sometimes be null.In a full outer join, there are no guarantees about l or r. Either one of them could
be a default record, but they will never both be a default record at the same time.To get non-null values for the output record, check both l and r to see which contains
the desired values.The example below defines a function for the as parameter that appropriately handles
the uncertainty of a full outer join.v_left and v_right still use values from l and r directly, because we expect
them to sometimes be null in the output table.

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
        
        method 
        - (Required)
String that specifies the join method.Supported methods:
        
        left 
        - Left input stream. Default is piped-forward data (<-).
        
    """
    name = "tables"
    package="join"

    def __init__(self, right, on, as_, method, left=None, ):
            super().__init__(right=right, on=on, as_=as_, method=method, left=left, )