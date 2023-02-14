from flux_query_builder.functions.base import FluxQueryFunction

class Tail(FluxQueryFunction):
    """tail() limits each output table to the last n rows.tail() produces one output table for each input table.
Each output table contains the last n records before the offset.
If the input table has less than offset + n records, tail() outputs all
records before the offset.(Required)
Maximum number of rows to output.Number of records to skip at the end of a table table before
limiting to n. Default is 0.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Maximum number of rows to output.
        
        offset 
        - Number of records to skip at the end of a table table before
limiting to n. Default is 0.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "tail"
    package=None

    def __init__(self, n, offset=None, tables=None, ):
            super().__init__(n=n, offset=offset, tables=tables, )