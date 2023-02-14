from flux_query_builder.functions.base import FluxQueryFunction

class Rate(FluxQueryFunction):
    """aggregate.rate() calculates the average rate of increase per window of time for each
input table.aggregate.rate() requires that input data have _start and _stop columns
to calculate windows of time to operate on.
Use range() to assign _start and _stop values.This function is designed to replicate the
Prometheus rate() function
and should only be used with counters.(Required)
Duration of time windows.List of columns to group by. Default is [].Time duration to use when calculating the rate. Default is 1s.Input data. Default is piped-forward data (<-).

    Params:
        
        every 
        - (Required)
Duration of time windows.
        
        groupColumns 
        - List of columns to group by. Default is [].
        
        unit 
        - Time duration to use when calculating the rate. Default is 1s.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "rate"
    package="aggregate"

    def __init__(self, every, groupColumns=None, unit=None, tables=None, ):
            super().__init__(every=every, groupColumns=groupColumns, unit=unit, tables=tables, )