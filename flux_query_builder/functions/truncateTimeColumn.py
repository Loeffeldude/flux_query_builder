from flux_query_builder.functions.base import FluxQueryFunction

class TruncateTimeColumn(FluxQueryFunction):
    """truncateTimeColumn() truncates all input time values in the _time to a
specified unit.When truncating a time value to the week (1w), weeks are determined using the
Unix epoch (1970-01-01T00:00:00Z UTC). The Unix epoch was on a Thursday,
so all calculated weeks begin on Thursday.(Required)
Unit of time to truncate to.Example units:Time column to truncate. Default is _time.Note: Currently, assigning a custom value to this parameter will have
no effect.Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - (Required)
Unit of time to truncate to.Example units:
        
        timeColumn 
        - Time column to truncate. Default is _time.Note: Currently, assigning a custom value to this parameter will have
no effect.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "truncateTimeColumn"
    package=None

    def __init__(self, unit, timeColumn=None, tables=None, ):
            super().__init__(unit=unit, timeColumn=timeColumn, tables=tables, )