from flux_query_builder.functions.base import FluxQueryFunction

class ShapeData(FluxQueryFunction):
    """geo.shapeData() renames existing latitude and longitude fields to lat and lon
and adds an s2_cell_id tag.Use geo.shapeData() to ensure geotemporal data meets the requirements of the Geo package:(Required)
Name of the existing field that contains the latitude value in decimal degrees (WGS 84).Field is renamed to lat.(Required)
Name of the existing field that contains the longitude value in decimal degrees (WGS 84).Field is renamed to lon.(Required)
S2 cell level
to use when generating the S2 cell ID token.Input data. Default is piped-forward data (<-).

    Params:
        
        latField 
        - (Required)
Name of the existing field that contains the latitude value in decimal degrees (WGS 84).Field is renamed to lat.
        
        lonField 
        - (Required)
Name of the existing field that contains the longitude value in decimal degrees (WGS 84).Field is renamed to lon.
        
        level 
        - (Required)
S2 cell level
to use when generating the S2 cell ID token.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "shapeData"
    package="geo"

    def __init__(self, latField, lonField, level, tables=None, ):
            super().__init__(latField=latField, lonField=lonField, level=level, tables=tables, )