from flux_query_builder.functions.base import FluxQueryFunction

class Sample(FluxQueryFunction):
    """sample() selects a subset of the rows from each input table.Note: sample() drops empty tables.(Required)
Sample every Nth element.Position offset from the start of results where sampling begins.
Default is -1 (random offset).pos must be less than n. If pos is less than 0, a random offset is used.Column to operate on.Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Sample every Nth element.
        
        pos 
        - Position offset from the start of results where sampling begins.
Default is -1 (random offset).pos must be less than n. If pos is less than 0, a random offset is used.
        
        column 
        - Column to operate on.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "sample"
    package=None

    def __init__(self, n, pos=None, column=None, tables=None, ):
            super().__init__(n=n, pos=pos, column=column, tables=tables, )