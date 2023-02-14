from flux_query_builder.functions.base import FluxQueryFunction

class ObjectKeys(FluxQueryFunction):
    """experimental.objectKeys() returns an array of property keys in a specified record.(Required)
Record to return property keys from.

    Params:
        
        o 
        - (Required)
Record to return property keys from.
        
    """
    name = "objectKeys"
    package="experimental"

    def __init__(self, o, ):
            super().__init__(o=o, )