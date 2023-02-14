from flux_query_builder.functions.base import FluxQueryFunction

class Today(FluxQueryFunction):
    """today() returns the now() timestamp truncated to the day unit.

    Params:
        
    """
    name = "today"
    package=None

    def __init__(self, ):
            super().__init__()