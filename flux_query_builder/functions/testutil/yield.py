from flux_query_builder.functions.base import FluxQueryFunction

class YieldFunction(FluxQueryFunction):
    """testutil.yield() is the identity function.Any value.

    Params:
        
        v 
        - Any value.
        
    """
    def __init__(self, v=None, ):
            super().__init__("", v=v, )