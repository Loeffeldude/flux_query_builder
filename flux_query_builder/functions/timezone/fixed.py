from flux_query_builder.functions.base import FluxQueryFunction

class Fixed(FluxQueryFunction):
    """timezone.fixed() returns a location record with a fixed offset.(Required)
Fixed duration for the location offset.
This duration is the offset from UTC.

    Params:
        
        offset 
        - (Required)
Fixed duration for the location offset.
This duration is the offset from UTC.
        
    """
    name = "fixed"
    package="timezone"

    def __init__(self, offset, ):
            super().__init__(offset=offset, )