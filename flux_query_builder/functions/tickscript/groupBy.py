from flux_query_builder.functions.base import FluxQueryFunction

class GroupBy(FluxQueryFunction):
    """tickscript.groupBy() groups results by the _measurement column and other specified columns.This function is comparable to Kapacitor QueryNode .groupBy.Note: To group by time intervals, use window() or tickscript.selectWindow().(Required)
List of columns to group by.Input data. Default is piped-forward data (<-).

    Params:
        
        columns 
        - (Required)
List of columns to group by.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "groupBy"
    package="tickscript"

    def __init__(self, columns, tables=None, ):
            super().__init__(columns=columns, tables=tables, )