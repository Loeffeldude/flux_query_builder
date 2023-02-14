from flux_query_builder.functions.base import FluxQueryFunction

class TrimPrefix(FluxQueryFunction):
    """strings.trimPrefix() removes a prefix from a string. Strings that do not start with the prefix are returned unchanged.(Required)
String to trim.(Required)
Prefix to remove.

    Params:
        
        v 
        - (Required)
String to trim.
        
        prefix 
        - (Required)
Prefix to remove.
        
    """
    name = "trimPrefix"
    package="strings"

    def __init__(self, v, prefix, ):
            super().__init__(v=v, prefix=prefix, )