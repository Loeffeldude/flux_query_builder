from flux_query_builder.functions.base import FluxQueryFunction

class Keep(FluxQueryFunction):
    """keep() returns a stream of tables containing only the specified columns.Columns in the group key that are not specifed in the columns parameter or
identified by the fn parameter are removed from the group key and dropped
from output tables. keep() is the inverse of drop().Columns to keep in output tables. Cannot be used with fn.Predicate function that takes a column name as a parameter (column) and
returns a boolean indicating whether or not the column should be kept in
output tables. Cannot be used with columns.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - Columns to keep in output tables. Cannot be used with fn.
        
        fn 
        - Predicate function that takes a column name as a parameter (column) and
returns a boolean indicating whether or not the column should be kept in
output tables. Cannot be used with columns.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "keep"
    package=None

    def __init__(self, columns=None, fn=None, tables=None, ):
            super().__init__(columns=columns, fn=fn, tables=tables, )