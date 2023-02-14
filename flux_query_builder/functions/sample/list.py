from flux_query_builder.functions.base import FluxQueryFunction

class List(FluxQueryFunction):
    """sample.list() outputs information about available InfluxDB sample datasets.

    Params:
        
    """
    name = "list"
    package="sample"

    def __init__(self, ):
            super().__init__()