from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """pushbullet.endpoint() creates the endpoint for the Pushbullet API and sends a notification of type note.pushbullet.endpoint() is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the record used to generate the API request.
Requires an r parameter.mapFn accepts a table row (r) and returns a record that must include the
following properties (as defined in pushbullet.pushNote()):PushBullet API endpoint URL. Default is "https://api.pushbullet.com/v2/pushes".Pushbullet API token string. Default is "".

    Params:
        
        url 
        - PushBullet API endpoint URL. Default is "https://api.pushbullet.com/v2/pushes".
        
        token 
        - Pushbullet API token string. Default is "".
        
    """
    name = "endpoint"
    package="pushbullet"

    def __init__(self, url=None, token=None, ):
            super().__init__(url=url, token=token, )