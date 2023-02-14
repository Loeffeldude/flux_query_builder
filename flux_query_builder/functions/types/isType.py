from flux_query_builder.functions.base import FluxQueryFunction

class IsType(FluxQueryFunction):
    """types.isType() tests if a value is a specified type.(Required)
Value to test.(Required)
String describing the type to check against.Supported types:

    Params:
        
        v 
        - (Required)
Value to test.
        
        type 
        - (Required)
String describing the type to check against.Supported types:
        
    """
    name = "isType"
    package="types"

    def __init__(self, v, type, ):
            super().__init__(v=v, type=type, )