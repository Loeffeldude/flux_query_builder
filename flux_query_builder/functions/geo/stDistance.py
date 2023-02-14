from flux_query_builder.functions.base import FluxQueryFunction

class StDistance(FluxQueryFunction):
    """geo.stDistance() returns the distance from a given region to a specified GIS geometry.geo.stDistance is used as a helper function for geo.ST_Distance().(Required)
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
    name = "stDistance"
    package="geo"

    def __init__(self, region, geometry, units, ):
            super().__init__(region=region, geometry=geometry, units=units, )