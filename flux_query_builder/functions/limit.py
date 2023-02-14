from flux_query_builder.functions.base import FluxQueryFunction

class Limit(FluxQueryFunction):
    """limit() returns the first n rows after the specified offset from each input table.If an input table has less than offset + n rows, limit() returns all rows
after the offset.(Required)
Maximum number of rows to return.Number of rows to skip per table before limiting to n.
Default is 0.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Maximum number of rows to return.
        
        offset 
        - Number of rows to skip per table before limiting to n.
Default is 0.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "limit"
    package=None

    def __init__(self, n, offset=None, tables=None, ):
            super().__init__(n=n, offset=offset, tables=tables, )