from flux_query_builder.functions.base import FluxQueryFunction

class Duplicate(FluxQueryFunction):
    """duplicate() duplicates a specified column in a table.If the specified column is part of the group key, it will be duplicated, but
the duplicate column will not be part of the output’s group key.(Required)
Column to duplicate.(Required)
Name to assign to the duplicate column.If the as column already exists, it will be overwritten by the duplicated column.Input data. Default is piped-forward data (<-).

    Params:
        
        column 
        - (Required)
Column to duplicate.
        
        as_ 
        - (Required)
Name to assign to the duplicate column.If the as column already exists, it will be overwritten by the duplicated column.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "duplicate"
    package=None

    def __init__(self, column, as_, tables=None, ):
            super().__init__(column=column, as_=as_, tables=tables, )