from flux_query_builder.functions.base import FluxQueryFunction

class PushData(FluxQueryFunction):
    """pushbullet.pushData() sends a push notification to the Pushbullet API.URL of the PushBullet endpoint. Default is "https://api.pushbullet.com/v2/pushes".API token string. Default is "".(Required)
Data to send to the endpoint. Data is JSON-encoded and sent to the Pushbullet’s endpoint.For how to structure data, see the Pushbullet API documentation.

    Params:
        
        data 
        - (Required)
Data to send to the endpoint. Data is JSON-encoded and sent to the Pushbullet’s endpoint.For how to structure data, see the Pushbullet API documentation.
        
        url 
        - URL of the PushBullet endpoint. Default is "https://api.pushbullet.com/v2/pushes".
        
        token 
        - API token string. Default is "".
        
    """
    name = "pushData"
    package="pushbullet"

    def __init__(self, data, url=None, token=None, ):
            super().__init__(data=data, url=url, token=token, )