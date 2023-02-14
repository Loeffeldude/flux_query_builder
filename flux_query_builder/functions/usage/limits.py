from flux_query_builder.functions.base import FluxQueryFunction

class Limits(FluxQueryFunction):
    """usage.limits() returns a record containing usage limits for an InfluxDB Cloud organization.InfluxDB Cloud region URL.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).InfluxDB Cloud organization ID. Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).InfluxDB Cloud API token.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).

    Params:
        
        host 
        - InfluxDB Cloud region URL.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
        orgID 
        - InfluxDB Cloud organization ID. Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
        token 
        - InfluxDB Cloud API token.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
    """
    name = "limits"
    package="usage"

    def __init__(self, host=None, orgID=None, token=None, ):
            super().__init__(host=host, orgID=orgID, token=token, )