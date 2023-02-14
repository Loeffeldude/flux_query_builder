from flux_query_builder.functions.base import FluxQueryFunction

class Yesterday(FluxQueryFunction):
    """boundaries.yesterday() returns a record with start and stop boundary timestamps for yesterday.Yesterday is relative to now().

    Params:
        
    """
    name = "yesterday"
    package="boundaries"

    def __init__(self, ):
            super().__init__()