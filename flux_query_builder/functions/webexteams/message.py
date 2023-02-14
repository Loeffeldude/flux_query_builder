from flux_query_builder.functions.base import FluxQueryFunction

class Message(FluxQueryFunction):
    """webexteams.message() sends a single message to Webex
using the Webex messages API.Base URL of Webex API endpoint (without a trailing slash).
Default is https://webexapis.com.(Required)
Webex API access token.(Required)
Room ID to send the message to.(Required)
Plain text message.(Required)
Markdown formatted message.

    Params:
        
        token 
        - (Required)
Webex API access token.
        
        roomId 
        - (Required)
Room ID to send the message to.
        
        text 
        - (Required)
Plain text message.
        
        markdown 
        - (Required)
Markdown formatted message.
        
        url 
        - Base URL of Webex API endpoint (without a trailing slash).
Default is https://webexapis.com.
        
    """
    name = "message"
    package="webexteams"

    def __init__(self, token, roomId, text, markdown, url=None, ):
            super().__init__(token=token, roomId=roomId, text=text, markdown=markdown, url=url, )