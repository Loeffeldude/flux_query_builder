from flux_query_builder.functions.base import FluxQueryFunction

class ST_Length(FluxQueryFunction):
    """geo.ST_Length() returns the spherical length or distance
of the specified GIS geometry.(Required)
GIS geometry to test. Can be either point or linestring geometry.
Point geometry will always return 0.0.Record that defines the unit of measurement for distance.

    Params:
        
        geometry 
        - (Required)
GIS geometry to test. Can be either point or linestring geometry.
Point geometry will always return 0.0.
        
        units 
        - Record that defines the unit of measurement for distance.
        
    """
    name = "ST_Length"
    package="geo"

    def __init__(self, geometry, units=None, ):
            super().__init__(geometry=geometry, units=units, )