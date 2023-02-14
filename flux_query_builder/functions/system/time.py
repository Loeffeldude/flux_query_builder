from flux_query_builder.functions.base import FluxQueryFunction

class Time(FluxQueryFunction):
    """system.time() returns the current system time.

    Params:
        
    """
    name = "time"
    package="system"

    def __init__(self, ):
            super().__init__()