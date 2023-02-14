from flux_query_builder.functions.base import FluxQueryFunction

class Send(FluxQueryFunction):
    """discord.send() sends a single message to a Discord channel using a Discord webhook.(Required)
Discord webhook token.(Required)
Discord webhook ID.(Required)
Override the Discord webhook’s default username.(Required)
Message to send to Discord (2000 character limit).Override the Discord webhook’s default avatar.

    Params:
        
        webhookToken 
        - (Required)
Discord webhook token.
        
        webhookID 
        - (Required)
Discord webhook ID.
        
        username 
        - (Required)
Override the Discord webhook’s default username.
        
        content 
        - (Required)
Message to send to Discord (2000 character limit).
        
        avatar_url 
        - Override the Discord webhook’s default avatar.
        
    """
    name = "send"
    package="discord"

    def __init__(self, webhookToken, webhookID, username, content, avatar_url=None, ):
            super().__init__(webhookToken=webhookToken, webhookID=webhookID, username=username, content=content, avatar_url=avatar_url, )