from flux_query_builder.functions.base import FluxQueryFunction

class StLength(FluxQueryFunction):
    """geo.stLength() returns the spherical length or distance
of the specified GIS geometry.geo.stLength is used as a helper function for geo.ST_Length().(Required)
GIS geometry to test. Can be either point or linestring geometry.
Point geometry will always return 0.0.(Required)
Record that defines the unit of measurement for distance.

    Params:
        
        geometry 
        - (Required)
GIS geometry to test. Can be either point or linestring geometry.
Point geometry will always return 0.0.
        
        units 
        - (Required)
Record that defines the unit of measurement for distance.
        
    """
    name = "stLength"
    package="geo"

    def __init__(self, geometry, units, ):
            super().__init__(geometry=geometry, units=units, )