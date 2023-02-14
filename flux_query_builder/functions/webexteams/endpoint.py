from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """webexteams.endpoint() returns a function that sends a message that includes data from input rows to a Webex room.webexteams.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see webexteams.message parameters.Base URL of Webex API endpoint (without a trailing slash).
Default is https://webexapis.com.(Required)
Webex API access token.

    Params:
        
        token 
        - (Required)
Webex API access token.
        
        url 
        - Base URL of Webex API endpoint (without a trailing slash).
Default is https://webexapis.com.
        
    """
    name = "endpoint"
    package="webexteams"

    def __init__(self, token, url=None, ):
            super().__init__(token=token, url=url, )