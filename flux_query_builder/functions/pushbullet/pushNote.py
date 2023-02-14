from flux_query_builder.functions.base import FluxQueryFunction

class PushNote(FluxQueryFunction):
    """pushbullet.pushNote() sends a push notification of type “note” to the Pushbullet API.URL of the PushBullet endpoint. Default is "https://api.pushbullet.com/v2/pushes".API token string. Defaults to: "".(Required)
Title of the notification.(Required)
Text to display in the notification.

    Params:
        
        title 
        - (Required)
Title of the notification.
        
        text 
        - (Required)
Text to display in the notification.
        
        url 
        - URL of the PushBullet endpoint. Default is "https://api.pushbullet.com/v2/pushes".
        
        token 
        - API token string. Defaults to: "".
        
    """
    name = "pushNote"
    package="pushbullet"

    def __init__(self, title, text, url=None, token=None, ):
            super().__init__(title=title, text=text, url=url, token=token, )