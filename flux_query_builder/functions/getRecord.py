from flux_query_builder.functions.base import FluxQueryFunction

class GetRecord(FluxQueryFunction):
    """getRecord() extracts a row at a specified index from a table as a record.If the specified index is out of bounds, the function returns an error.(Required)
Index of the record to extract.Input table. Default is piped-forward data (<-).

    Params:
        
        idx 
        - (Required)
Index of the record to extract.
        
        table 
        - Input table. Default is piped-forward data (<-).
        
    """
    name = "getRecord"
    package=None

    def __init__(self, idx, table=None, ):
            super().__init__(idx=idx, table=table, )