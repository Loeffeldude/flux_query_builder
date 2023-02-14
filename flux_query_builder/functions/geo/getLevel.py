from flux_query_builder.functions.base import FluxQueryFunction

class GetLevel(FluxQueryFunction):
    """geo.getLevel() returns the S2 cell level of specified cell ID token.(Required)
S2 cell ID token.

    Params:
        
        token 
        - (Required)
S2 cell ID token.
        
    """
    name = "getLevel"
    package="geo"

    def __init__(self, token, ):
            super().__init__(token=token, )