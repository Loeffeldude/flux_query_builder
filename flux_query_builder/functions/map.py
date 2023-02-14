from flux_query_builder.functions.base import FluxQueryFunction

class Map(FluxQueryFunction):
    """map() iterates over and applies a function to input rows.Each input row is passed to the fn as a record, r.
Each r property represents a column key-value pair.
Output values must be of the following supported column types:Output tables are the result of applying the map function (fn) to each
record of the input tables. Output records are assigned to new tables based
on the group key of the input stream.
If the output record contains a different value for a group key column, the
record is regrouped into the appropriate table.
If the output record drops a group key column, that column is removed from
the group key.map() drops any columns that are not mapped explictly by column label or
implicitly using the with operator in the fn function.
The with operator updates a record property if it already exists, creates
a new record property if it doesn’t exist, and includes all existing
properties in the output record.(Required)
Single argument function to apply to each record.
The return value must be a record.(Deprecated) Merge group keys of mapped records. Default is false.Input data. Default is piped-forward data (<-).Use the with operator on the r record to preserve columns not directly
operated on by the map operation.

    Params:
        
        fn 
        - (Required)
Single argument function to apply to each record.
The return value must be a record.
        
        mergeKey 
        - (Deprecated) Merge group keys of mapped records. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "map"
    package=None

    def __init__(self, fn, mergeKey=None, tables=None, ):
            super().__init__(fn=fn, mergeKey=mergeKey, tables=tables, )