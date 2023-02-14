from flux_query_builder.functions.base import FluxQueryFunction

class TimeWeightedAvg(FluxQueryFunction):
    """timeWeightedAvg() returns the time-weighted average of non-null values in
_value column as a float for each input table.Time is weighted using the linearly interpolated integral of values in the table.(Required)
Unit of time to use to compute the time-weighted average.Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - (Required)
Unit of time to use to compute the time-weighted average.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "timeWeightedAvg"
    package=None

    def __init__(self, unit, tables=None, ):
            super().__init__(unit=unit, tables=tables, )