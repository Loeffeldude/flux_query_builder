from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """victorops.endpoint() sends events to VictorOps using data from input rows.victorops.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see victorops.event() parameters.(Required)
VictorOps REST endpoint integration URL.Example: https://alert.victorops.com/integrations/generic/00000000/alert/<api_key>/<routing_key>
Replace <api_key> and <routing_key> with valid VictorOps API and routing keys.Tool to use for monitoring.
Default is InfluxDB.

    Params:
        
        url 
        - (Required)
VictorOps REST endpoint integration URL.Example: https://alert.victorops.com/integrations/generic/00000000/alert/<api_key>/<routing_key>
Replace <api_key> and <routing_key> with valid VictorOps API and routing keys.
        
        monitoringTool 
        - Tool to use for monitoring.
Default is InfluxDB.
        
    """
    name = "endpoint"
    package="victorops"

    def __init__(self, url, monitoringTool=None, ):
            super().__init__(url=url, monitoringTool=monitoringTool, )