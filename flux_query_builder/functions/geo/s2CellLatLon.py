from flux_query_builder.functions.base import FluxQueryFunction

class S2CellLatLon(FluxQueryFunction):
    """geo.s2CellLatLon() returns the latitude and longitude of the center of an S2 cell.(Required)
S2 cell ID token.

    Params:
        
        token 
        - (Required)
S2 cell ID token.
        
    """
    name = "s2CellLatLon"
    package="geo"

    def __init__(self, token, ):
            super().__init__(token=token, )