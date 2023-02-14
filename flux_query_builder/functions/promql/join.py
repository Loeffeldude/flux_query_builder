from flux_query_builder.functions.base import FluxQueryFunction

class Join(FluxQueryFunction):
    """promql.join() joins two streams of tables on the group key and _time column.
See experimental.join.Important: The internal/promql package is not meant for external use.(Required)
First of two streams of tables to join.(Required)
Second of two streams of tables to join.(Required)
Function with left and right arguments that maps a new output record
using values from the left and right input records.
The return value must be a record.

    Params:
        
        left 
        - (Required)
First of two streams of tables to join.
        
        right 
        - (Required)
Second of two streams of tables to join.
        
        fn 
        - (Required)
Function with left and right arguments that maps a new output record
using values from the left and right input records.
The return value must be a record.
        
    """
    name = "join"
    package="promql"

    def __init__(self, left, right, fn, ):
            super().__init__(left=left, right=right, fn=fn, )