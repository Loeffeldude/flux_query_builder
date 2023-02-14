from flux_query_builder.functions.base import FluxQueryFunction

class Tuesday(FluxQueryFunction):
    """boundaries.tuesday() returns a record with start and stop boundary timestamps of last Tuesday.Last Tuesday is relative to now(). If today is Tuesday, the function returns boundaries for the previous Tuesday.

    Params:
        
    """
    name = "tuesday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()