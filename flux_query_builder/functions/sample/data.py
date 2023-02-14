from flux_query_builder.functions.base import FluxQueryFunction

class Data(FluxQueryFunction):
    """sample.data() downloads a specified InfluxDB sample dataset.(Required)
Sample data set to download and output.Valid datasets:

    Params:
        
        set 
        - (Required)
Sample data set to download and output.Valid datasets:
        
    """
    name = "data"
    package="sample"

    def __init__(self, set, ):
            super().__init__(set=set, )