from flux_query_builder.functions.base import FluxQueryFunction

class Saturday(FluxQueryFunction):
    """boundaries.saturday() returns a record with start and stop boundary timestamps for last Saturday.Last Saturday is relative to now(). If today is Saturday, the function returns boundaries for the previous Saturday.

    Params:
        
    """
    name = "saturday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()