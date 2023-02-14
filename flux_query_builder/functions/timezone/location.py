from flux_query_builder.functions.base import FluxQueryFunction

class Location(FluxQueryFunction):
    """timezone.location() returns a location record based on a location or timezone name.(Required)
Location name (as defined by your operating system timezone database).

    Params:
        
        name 
        - (Required)
Location name (as defined by your operating system timezone database).
        
    """
    name = "location"
    package="timezone"

    def __init__(self, name, ):
            super().__init__(name=name, )