from flux_query_builder.functions.base import FluxQueryFunction

class AsArray(FluxQueryFunction):
    """dynamic.asArray() converts a dynamic value into an array of dynamic elements.The dynamic input value must be an array. If it is not an array, dynamic.asArray() returns an error.Dynamic value to convert. Default is the piped-forward value (<-).

    Params:
        
        v 
        - Dynamic value to convert. Default is the piped-forward value (<-).
        
    """
    name = "asArray"
    package="dynamic"

    def __init__(self, v=None, ):
            super().__init__(v=v, )