from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """teams.endpoint() sends a message to a Microsoft Teams channel using data from table rows.teams.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see teams.message parameters.(Required)
Incoming webhook URL.

    Params:
        
        url 
        - (Required)
Incoming webhook URL.
        
    """
    name = "endpoint"
    package="teams"

    def __init__(self, url, ):
            super().__init__(url=url, )