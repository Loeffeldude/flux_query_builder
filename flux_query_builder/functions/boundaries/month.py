from flux_query_builder.functions.base import FluxQueryFunction

class Month(FluxQueryFunction):
    """boundaries.month() returns a record with start and stop boundary timestamps for the current month.now() determines the current month.Number of months to offset from the current month. Default is 0.Use a negative offset to return boundaries from previous months.
Use a positive offset to return boundaries for future months.

    Params:
        
        month_offset 
        - Number of months to offset from the current month. Default is 0.Use a negative offset to return boundaries from previous months.
Use a positive offset to return boundaries for future months.
        
    """
    name = "month"
    package="boundaries"

    def __init__(self, month_offset=None, ):
            super().__init__(month_offset=month_offset, )