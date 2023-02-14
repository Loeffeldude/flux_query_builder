from flux_query_builder.functions.base import FluxQueryFunction

class Wednesday(FluxQueryFunction):
    """boundaries.wednesday() returns a record with start and stop boundary timestamps for last Wednesday.Last Wednesday is relative to now(). If today is Wednesday, the function returns boundaries for the previous Wednesday.

    Params:
        
    """
    name = "wednesday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()