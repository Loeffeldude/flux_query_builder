from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """zenoss.endpoint() sends events to Zenoss using data from input rows.zenoss.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see zenoss.event() parameters.(Required)
Zenoss router endpoint URL.Zenoss username to use for HTTP BASIC authentication.
Default is "" (no authentication).Zenoss password to use for HTTP BASIC authentication.
Default is "" (no authentication).Zenoss cloud API key.
Default is "" (no API key).Zenoss router name.
Default is "EventsRouter".EventsRouter method.
Default is "add_event".Event type. Default is "rpc".Temporary request transaction ID.
Default is 1.

    Params:
        
        url 
        - (Required)
Zenoss router endpoint URL.
        
        username 
        - Zenoss username to use for HTTP BASIC authentication.
Default is "" (no authentication).
        
        password 
        - Zenoss password to use for HTTP BASIC authentication.
Default is "" (no authentication).
        
        apiKey 
        - Zenoss cloud API key.
Default is "" (no API key).
        
        action 
        - Zenoss router name.
Default is "EventsRouter".
        
        method 
        - EventsRouter method.
Default is "add_event".
        
        type 
        - Event type. Default is "rpc".
        
        tid 
        - Temporary request transaction ID.
Default is 1.
        
    """
    name = "endpoint"
    package="zenoss"

    def __init__(self, url, username=None, password=None, apiKey=None, action=None, method=None, type=None, tid=None, ):
            super().__init__(url=url, username=username, password=password, apiKey=apiKey, action=action, method=method, type=type, tid=tid, )