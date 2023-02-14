from flux_query_builder.functions.base import FluxQueryFunction

class Drop(FluxQueryFunction):
    """drop() removes specified columns from a table.Columns are specified either through a list or a predicate function.
When a dropped column is part of the group key, it is removed from the key.
If a specified column is not present in a table, the function returns an error.List of columns to remove from input tables. Mutually exclusive with fn.Predicate function with a column parameter that returns a boolean
value indicating whether or not the column should be removed from input tables.
Mutually exclusive with columns.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - List of columns to remove from input tables. Mutually exclusive with fn.
        
        fn 
        - Predicate function with a column parameter that returns a boolean
value indicating whether or not the column should be removed from input tables.
Mutually exclusive with columns.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "drop"
    package=None

    def __init__(self, columns=None, fn=None, tables=None, ):
            super().__init__(columns=columns, fn=fn, tables=tables, )