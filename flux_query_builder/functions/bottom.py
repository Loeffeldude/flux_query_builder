from flux_query_builder.functions.base import FluxQueryFunction

class Bottom(FluxQueryFunction):
    """bottom() sorts each input table by specified columns and keeps the bottom n
records in each table.Note: bottom() drops empty tables.(Required)
Number of rows to return from each input table.List of columns to sort by. Default is ["_value"].Sort precedence is determined by list order (left to right).Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of rows to return from each input table.
        
        columns 
        - List of columns to sort by. Default is ["_value"].Sort precedence is determined by list order (left to right).
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "bottom"
    package=None

    def __init__(self, n, columns=None, tables=None, ):
            super().__init__(n=n, columns=columns, tables=tables, )