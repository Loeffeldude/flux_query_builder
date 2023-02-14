from flux_query_builder.functions.base import FluxQueryFunction

class Sunday(FluxQueryFunction):
    """boundaries.sunday() returns a record with start and stop boundary timestamps for last Sunday.Last Sunday is relative to now(). If today is Sunday, the function returns boundaries for the previous Sunday.

    Params:
        
    """
    name = "sunday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()