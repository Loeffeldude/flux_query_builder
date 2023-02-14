from flux_query_builder.functions.base import FluxQueryFunction

class TableFind(FluxQueryFunction):
    """tableFind() extracts the first table in a stream with group key values that
match a specified predicate.(Required)
Predicate function to evaluate input table group keys.tableFind() returns the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Predicate function to evaluate input table group keys.tableFind() returns the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "tableFind"
    package=None

    def __init__(self, fn, tables=None, ):
            super().__init__(fn=fn, tables=tables, )