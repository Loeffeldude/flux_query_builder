from flux_query_builder.functions.base import FluxQueryFunction

class Set(FluxQueryFunction):
    """set() assigns a static column value to each row in the input tables.set() may modify an existing column or add a new column.
If the modified column is part of the group key, output tables are regrouped as needed.
set() can only set string values.(Required)
Label of the column to modify or set.(Required)
String value to set.Input data. Default is piped-forward data (<-).

    Params:
        
        key 
        - (Required)
Label of the column to modify or set.
        
        value 
        - (Required)
String value to set.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "set"
    package=None

    def __init__(self, key, value, tables=None, ):
            super().__init__(key=key, value=value, tables=tables, )