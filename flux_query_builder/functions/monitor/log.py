from flux_query_builder.functions.base import FluxQueryFunction

class Log(FluxQueryFunction):
    """monitor.log() persists notification events to an InfluxDB bucket.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "log"
    package="monitor"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )