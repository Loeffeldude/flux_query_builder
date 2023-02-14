from flux_query_builder.functions.base import FluxQueryFunction

class Thursday(FluxQueryFunction):
    """boundaries.thursday() returns a record with start and stop boundary timestamps for last Thursday.Last Thursday is relative to now(). If today is Thursday, the function returns boundaries for the previous Thursday.

    Params:
        
    """
    name = "thursday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()