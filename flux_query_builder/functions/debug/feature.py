from flux_query_builder.functions.base import FluxQueryFunction

class Feature(FluxQueryFunction):
    """debug.feature() returns the value associated with the given feature flag.(Required)
Feature flag name.

    Params:
        
        key 
        - (Required)
Feature flag name.
        
    """
    name = "feature"
    package="debug"

    def __init__(self, key, ):
            super().__init__(key=key, )