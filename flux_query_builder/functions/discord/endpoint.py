from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """discord.endpoint() sends a single message to a Discord channel using a
Discord webhook
and data from table rows.discord.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the record used to generate the Discord webhook request.
Requires an r parameter.mapFn accepts a table row (r) and returns a record that must include the following field:For more information, see the discord.send() content parameter.(Required)
Discord webhook token.(Required)
Discord webhook ID.(Required)
Override the Discord webhook’s default username.Override the Discord webhook’s default avatar.

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
        
        avatar_url 
        - Override the Discord webhook’s default avatar.
        
    """
    name = "endpoint"
    package="discord"

    def __init__(self, webhookToken, webhookID, username, avatar_url=None, ):
            super().__init__(webhookToken=webhookToken, webhookID=webhookID, username=username, avatar_url=avatar_url, )