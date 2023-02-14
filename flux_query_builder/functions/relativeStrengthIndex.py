from flux_query_builder.functions.base import FluxQueryFunction

class RelativeStrengthIndex(FluxQueryFunction):
    """relativeStrengthIndex() measures the relative speed and change of values in input tables.For each input table with x rows, relativeStrengthIndex() outputs a table
with x - n rows.(Required)
Number of values to use to calculate the RSI.Columns to operate on. Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Number of values to use to calculate the RSI.
        
        columns 
        - Columns to operate on. Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "relativeStrengthIndex"
    package=None

    def __init__(self, n, columns=None, tables=None, ):
            super().__init__(n=n, columns=columns, tables=tables, )