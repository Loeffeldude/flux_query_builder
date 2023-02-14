from flux_query_builder.functions.base import FluxQueryFunction

class TrimSuffix(FluxQueryFunction):
    """strings.trimSuffix() removes a suffix from a string.Strings that do not end with the suffix are returned unchanged.(Required)
String to trim.(Required)
Suffix to remove.

    Params:
        
        v 
        - (Required)
String to trim.
        
        suffix 
        - (Required)
Suffix to remove.
        
    """
    name = "trimSuffix"
    package="strings"

    def __init__(self, v, suffix, ):
            super().__init__(v=v, suffix=suffix, )