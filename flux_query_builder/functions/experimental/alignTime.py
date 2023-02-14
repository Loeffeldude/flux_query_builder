from flux_query_builder.functions.base import FluxQueryFunction

class AlignTime(FluxQueryFunction):
    """experimental.alignTime() shifts time values in input tables to all start at a common start time.Time to align tables to. Default is 1970-01-01T00:00:00Z.Input data. Default is piped-forward data (<-).Each output table represents data from a calendar month.
When visualized, data is still grouped by month, but timestamps are aligned
to a common start time and values can be compared by time.

    Params:
        
        alignTo 
        - Time to align tables to. Default is 1970-01-01T00:00:00Z.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "alignTime"
    package="experimental"

    def __init__(self, alignTo=None, tables=None, ):
            super().__init__(alignTo=alignTo, tables=tables, )