from flux_query_builder.functions.base import FluxQueryFunction

class Yield(FluxQueryFunction):
    """testutil.yield() is the identity function.Any value.

    Params:
        
        v 
        - Any value.
        
    """
    name = "yield"
    package="testutil"

    def __init__(self, v=None, ):
            super().__init__(v=v, )