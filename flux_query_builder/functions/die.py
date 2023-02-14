from flux_query_builder.functions.base import FluxQueryFunction

class Die(FluxQueryFunction):
    """die() stops the Flux script execution and returns an error message.(Required)
Error message to return.

    Params:
        
        msg 
        - (Required)
Error message to return.
        
    """
    name = "die"
    package=None

    def __init__(self, msg, ):
            super().__init__(msg=msg, )