from flux_query_builder.functions.base import FluxQueryFunction

class ST_Distance(FluxQueryFunction):
    """geo.ST_Distance() returns the distance from a given region to a specified GIS geometry.(Required)
Region to test. Specify record properties for the shape.(Required)
GIS geometry to test. Can be either point or linestring geometry.Record that defines the unit of measurement for distance.
Default is the geo.units option.

    Params:
        
        region 
        - (Required)
Region to test. Specify record properties for the shape.
        
        geometry 
        - (Required)
GIS geometry to test. Can be either point or linestring geometry.
        
        units 
        - Record that defines the unit of measurement for distance.
Default is the geo.units option.
        
    """
    name = "ST_Distance"
    package="geo"

    def __init__(self, region, geometry, units=None, ):
            super().__init__(region=region, geometry=geometry, units=units, )