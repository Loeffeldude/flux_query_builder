from flux_query_builder.functions.base import FluxQueryFunction

class AlignToNow(FluxQueryFunction):
    """sample.alignToNow() shifts time values in input data to align the chronological last point to now.When writing static historical sample datasets to InfluxDB Cloud, use alignToNow()
to avoid losing sample data with timestamps outside of the retention period
associated with your InfluxDB Cloud account.Input data must have a _time column.Input data. Defaults to piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Defaults to piped-forward data (<-).
        
    """
    name = "alignToNow"
    package="sample"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )