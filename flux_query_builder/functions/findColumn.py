from flux_query_builder.functions.base import FluxQueryFunction

class FindColumn(FluxQueryFunction):
    """findColumn() returns an array of values in a specified column from the first
table in a stream of tables that matches the specified predicate function.The function returns an empty array if no table is found or if the column
label is not present in the set of columns.(Required)
Column to extract.(Required)
Predicate function to evaluate input table group keys.findColumn() uses the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - (Required)
Column to extract.
        
        fn 
        - (Required)
Predicate function to evaluate input table group keys.findColumn() uses the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "findColumn"
    package=None

    def __init__(self, column, fn, tables=None, ):
            super().__init__(column=column, fn=fn, tables=tables, )