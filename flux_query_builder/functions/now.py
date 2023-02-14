from flux_query_builder.functions.base import FluxQueryFunction

class Now(FluxQueryFunction):
    """now() is a function option that, by default, returns the current system time.now() returns the current system time (UTC). now() is cached at runtime,
so all executions of now() in a Flux script return the same time value.
system.time() returns the system time (UTC) at which system.time() is executed.
Each instance of system.time() in a Flux script returns a unique value.

    Params:
        
    """
    name = "now"
    package=None

    def __init__(self, ):
            super().__init__()