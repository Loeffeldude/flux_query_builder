from flux_query_builder.functions.base import FluxQueryFunction

class ST_DWithin(FluxQueryFunction):
    """geo.ST_DWithin() tests if the specified region is within a defined distance from
the specified GIS geometry and returns true or false.(Required)
Region to test. Specify record properties for the shape.(Required)
GIS geometry to test. Can be either point or linestring geometry.(Required)
Maximum distance allowed between the region and geometry.
Define distance units with the geo.units option.Record that defines the unit of measurement for distance.
Default is the geo.units option.

    Params:
        
        region 
        - (Required)
Region to test. Specify record properties for the shape.
        
        geometry 
        - (Required)
GIS geometry to test. Can be either point or linestring geometry.
        
        distance 
        - (Required)
Maximum distance allowed between the region and geometry.
Define distance units with the geo.units option.
        
        units 
        - Record that defines the unit of measurement for distance.
Default is the geo.units option.
        
    """
    name = "ST_DWithin"
    package="geo"

    def __init__(self, region, geometry, distance, units=None, ):
            super().__init__(region=region, geometry=geometry, distance=distance, units=units, )