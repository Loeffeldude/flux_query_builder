from flux_query_builder.functions.base import FluxQueryFunction

class S2CellIDToken(FluxQueryFunction):
    """geo.s2CellIDToken() returns and S2 cell ID token for given cell or point at a
specified S2 cell level.S2 cell ID token to update.Useful for changing the S2 cell level of an existing S2 cell ID token.Record with lat and lon properties that specify the latitude and
longitude in decimal degrees (WGS 84) of a point.(Required)
S2 cell level to use when generating the S2 cell ID token.

    Params:
        
        level 
        - (Required)
S2 cell level to use when generating the S2 cell ID token.
        
        token 
        - S2 cell ID token to update.Useful for changing the S2 cell level of an existing S2 cell ID token.
        
        point 
        - Record with lat and lon properties that specify the latitude and
longitude in decimal degrees (WGS 84) of a point.
        
    """
    name = "s2CellIDToken"
    package="geo"

    def __init__(self, level, token=None, point=None, ):
            super().__init__(level=level, token=token, point=point, )