from flux_query_builder.functions.base import FluxQueryFunction

class FindRecord(FluxQueryFunction):
    """findRecord() returns a row at a specified index as a record from the first
table in a stream of tables that matches the specified predicate function.The function returns an empty record if no table is found or if the index is
out of bounds.(Required)
Index of the record to extract.(Required)
Predicate function to evaluate input table group keys.findColumn() uses the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.Input data. Default is piped-forward data (<-).

    Params:
        
        idx 
        - (Required)
Index of the record to extract.
        
        fn 
        - (Required)
Predicate function to evaluate input table group keys.findColumn() uses the first table that resolves as true.
The predicate function requires a key argument that represents each input
table’s group key as a record.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "findRecord"
    package=None

    def __init__(self, idx, fn, tables=None, ):
            super().__init__(idx=idx, fn=fn, tables=tables, )