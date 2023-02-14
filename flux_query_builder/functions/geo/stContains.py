from flux_query_builder.functions.base import FluxQueryFunction

class StContains(FluxQueryFunction):
    """geo.stContains() returns boolean indicating whether the defined region contains a specified GIS geometry.geo.stContains is used as a helper function for geo.ST_Contains().(Required)
Region to test. Specify record properties for the shape.(Required)
GIS geometry to test. Can be either point or linestring geometry.(Required)
Record that defines the unit of measurement for distance.

    Params:
        
        region 
        - (Required)
Region to test. Specify record properties for the shape.
        
        geometry 
        - (Required)
GIS geometry to test. Can be either point or linestring geometry.
        
        units 
        - (Required)
Record that defines the unit of measurement for distance.
        
    """
    name = "stContains"
    package="geo"

    def __init__(self, region, geometry, units, ):
            super().__init__(region=region, geometry=geometry, units=units, )