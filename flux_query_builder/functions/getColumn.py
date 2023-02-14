from flux_query_builder.functions.base import FluxQueryFunction

class GetColumn(FluxQueryFunction):
    """getColumn() extracts a specified column from a table as an array.If the specified column is not present in the table, the function returns an error.(Required)
Column to extract.Input table. Default is piped-forward data (<-).

    Params:
        
        column 
        - (Required)
Column to extract.
        
        table 
        - Input table. Default is piped-forward data (<-).
        
    """
    name = "getColumn"
    package=None

    def __init__(self, column, table=None, ):
            super().__init__(column=column, table=table, )