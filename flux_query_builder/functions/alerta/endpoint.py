from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """alerta.endpoint() sends alerts to Alerta using data from input rows.alerta.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see alerta.alert() parameters.(Required)
(Required) Alerta URL.(Required)
(Required) Alerta API key.Alert environment. Default is "".
Valid values: “Production”, “Development”, or empty string (default).Alert origin. Default is "InfluxDB".

    Params:
        
        url 
        - (Required)
(Required) Alerta URL.
        
        apiKey 
        - (Required)
(Required) Alerta API key.
        
        environment 
        - Alert environment. Default is "".
Valid values: “Production”, “Development”, or empty string (default).
        
        origin 
        - Alert origin. Default is "InfluxDB".
        
    """
    name = "endpoint"
    package="alerta"

    def __init__(self, url, apiKey, environment=None, origin=None, ):
            super().__init__(url=url, apiKey=apiKey, environment=environment, origin=origin, )