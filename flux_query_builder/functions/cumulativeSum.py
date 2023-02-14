from flux_query_builder.functions.base import FluxQueryFunction

class CumulativeSum(FluxQueryFunction):
    """cumulativeSum() computes a running sum for non-null records in a table.The output table schema will be the same as the input table.List of columns to operate on. Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - List of columns to operate on. Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "cumulativeSum"
    package=None

    def __init__(self, columns=None, tables=None, ):
            super().__init__(columns=columns, tables=tables, )