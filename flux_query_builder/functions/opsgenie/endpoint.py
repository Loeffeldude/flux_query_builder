from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """opsgenie.endpoint() sends an alert message to Opsgenie using data from table rows.opsgenie.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the record used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns a record that must include the following fields:For more information, see opsgenie.sendAlert.Opsgenie API URL. Defaults to https://api.opsgenie.com/v2/alerts.(Required)
(Required) Opsgenie API authorization key.Alert entity used to specify the alert domain.

    Params:
        
        apiKey 
        - (Required)
(Required) Opsgenie API authorization key.
        
        url 
        - Opsgenie API URL. Defaults to https://api.opsgenie.com/v2/alerts.
        
        entity 
        - Alert entity used to specify the alert domain.
        
    """
    name = "endpoint"
    package="opsgenie"

    def __init__(self, apiKey, url=None, entity=None, ):
            super().__init__(apiKey=apiKey, url=url, entity=entity, )