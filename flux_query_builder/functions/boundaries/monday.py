from flux_query_builder.functions.base import FluxQueryFunction

class Monday(FluxQueryFunction):
    """boundaries.monday() returns a record with start and stop boundary timestamps of last Monday.
Last Monday is relative to now(). If today is Monday, the function returns boundaries for the previous Monday.

    Params:
        
    """
    name = "monday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()