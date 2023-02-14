from flux_query_builder.functions.base import FluxQueryFunction

class LowestMin(FluxQueryFunction):
    """lowestMin() selects the record with the lowest value in the specified column
from each input table and returns the bottom n records.Note: lowestMin() drops empty tables.(Required)
Number of records to return.Column to evaluate. Default is _value.List of columns to group by. Default is [].Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of records to return.
        
        column 
        - Column to evaluate. Default is _value.
        
        groupColumns 
        - List of columns to group by. Default is [].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "lowestMin"
    package=None

    def __init__(self, n, column=None, groupColumns=None, tables=None, ):
            super().__init__(n=n, column=column, groupColumns=groupColumns, tables=tables, )