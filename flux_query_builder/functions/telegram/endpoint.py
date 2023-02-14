from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """telegram.endpoint() sends a message to a Telegram channel using data from table rows.telegram.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see telegram.message() parameters.See telegram.message parameters for more information.URL of the Telegram bot endpoint. Default is https://api.telegram.org/bot.(Required)
Telegram bot token.Parse mode
of the message text.
Default is MarkdownV2.Disable preview of web links in the sent message.
Default is false.

    Params:
        
        token 
        - (Required)
Telegram bot token.
        
        url 
        - URL of the Telegram bot endpoint. Default is https://api.telegram.org/bot.
        
        parseMode 
        - Parse mode
of the message text.
Default is MarkdownV2.
        
        disableWebPagePreview 
        - Disable preview of web links in the sent message.
Default is false.
        
    """
    name = "endpoint"
    package="telegram"

    def __init__(self, token, url=None, parseMode=None, disableWebPagePreview=None, ):
            super().__init__(token=token, url=url, parseMode=parseMode, disableWebPagePreview=disableWebPagePreview, )