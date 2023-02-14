from flux_query_builder.functions.base import FluxQueryFunction

class Set(FluxQueryFunction):
    """experimental.set() sets multiple static column values on all records.If a column already exists, the function updates the existing value.
If a column does not exist, the function adds it with the specified value.(Required)
Record that defines the columns and values to set.The key of each key-value pair defines the column name.
The value of each key-value pair defines the column value.Input data. Default is piped-forward data (<-).

    Params:
        
        o 
        - (Required)
Record that defines the columns and values to set.The key of each key-value pair defines the column name.
The value of each key-value pair defines the column value.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "set"
    package="experimental"

    def __init__(self, o, tables=None, ):
            super().__init__(o=o, tables=tables, )