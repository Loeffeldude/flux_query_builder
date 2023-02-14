from flux_query_builder.functions.base import FluxQueryFunction

class Week(FluxQueryFunction):
    """boundaries.week() returns a record with start and stop boundary timestamps of the current week.
By default, weeks start on Monday.Indicate if the week starts on Sunday. Default is false.When set to false, the week starts on Monday.Number of weeks to offset from the current week. Default is 0.Use a negative offset to return boundaries from previous weeks.
Use a positive offset to return boundaries for future weeks.

    Params:
        
        start_sunday 
        - Indicate if the week starts on Sunday. Default is false.When set to false, the week starts on Monday.
        
        week_offset 
        - Number of weeks to offset from the current week. Default is 0.Use a negative offset to return boundaries from previous weeks.
Use a positive offset to return boundaries for future weeks.
        
    """
    name = "week"
    package="boundaries"

    def __init__(self, start_sunday=None, week_offset=None, ):
            super().__init__(start_sunday=start_sunday, week_offset=week_offset, )