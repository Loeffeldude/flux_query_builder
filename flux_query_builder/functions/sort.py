from flux_query_builder.functions.base import FluxQueryFunction

class Sort(FluxQueryFunction):
    """sort() orders rows in each intput table based on values in specified columns.One output table is produced for each input table.
Output tables have the same schema as their corresponding input tables.When desc: false, null values are last in the sort order.
When desc: true, null values are first in the sort order.List of columns to sort by. Default is ["_value"].Sort precedence is determined by list order (left to right).Sort results in descending order. Default is false.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - List of columns to sort by. Default is ["_value"].Sort precedence is determined by list order (left to right).
        
        desc 
        - Sort results in descending order. Default is false.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "sort"
    package=None

    def __init__(self, columns=None, desc=None, tables=None, ):
            super().__init__(columns=columns, desc=desc, tables=tables, )