from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """bigpanda.endpoint() sends alerts to BigPanda using data from input rows.bigpanda.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see bigpanda.sendAlert() parameters.BigPanda alerts API URL.
Default is the value of the bigpanda.defaultURL option.(Required)
BigPanda API Authorization token (API key).(Required)
BigPanda App Key.

    Params:
        
        token 
        - (Required)
BigPanda API Authorization token (API key).
        
        appKey 
        - (Required)
BigPanda App Key.
        
        url 
        - BigPanda alerts API URL.
Default is the value of the bigpanda.defaultURL option.
        
    """
    name = "endpoint"
    package="bigpanda"

    def __init__(self, token, appKey, url=None, ):
            super().__init__(token=token, appKey=appKey, url=url, )