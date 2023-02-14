from flux_query_builder.functions.base import FluxQueryFunction

class Write(FluxQueryFunction):
    """monitor.write() persists check statuses to an InfluxDB bucket.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "write"
    package="monitor"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )