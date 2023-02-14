from flux_query_builder.functions.base import FluxQueryFunction

class Friday(FluxQueryFunction):
    """boundaries.friday() returns a record with start and stop boundary timestamps for last Friday.Last Friday is relative to now(). If today is Friday, the function returns boundaries for the previous Friday.

    Params:
        
    """
    name = "friday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()