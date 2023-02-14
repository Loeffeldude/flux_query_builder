from flux_query_builder.functions.base import FluxQueryFunction

class Scale(FluxQueryFunction):
    """date.scale() will multiply the duration by the given value.(Required)
Duration to scale.(Required)
Amount to scale the duration by.

    Params:
        
        d 
        - (Required)
Duration to scale.
        
        n 
        - (Required)
Amount to scale the duration by.
        
    """
    name = "scale"
    package="date"

    def __init__(self, d, n, ):
            super().__init__(d=d, n=n, )