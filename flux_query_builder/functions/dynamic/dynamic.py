from flux_query_builder.functions.base import FluxQueryFunction

class Dynamic(FluxQueryFunction):
    """dynamic.dynamic() wraps a value so it can be used as a dynamic value.(Required)
Value to wrap as dynamic.

    Params:
        
        v 
        - (Required)
Value to wrap as dynamic.
        
    """
    name = "dynamic"
    package="dynamic"

    def __init__(self, v, ):
            super().__init__(v=v, )