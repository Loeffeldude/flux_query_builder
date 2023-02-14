from flux_query_builder.functions.base import FluxQueryFunction

class Message(FluxQueryFunction):
    """telegram.message() sends a single message to a Telegram channel
using the sendMessage method of the Telegram Bot API.URL of the Telegram bot endpoint. Default is https://api.telegram.org/bot.(Required)
Telegram bot token.(Required)
Telegram channel ID.(Required)
Message text.Parse mode
of the message text.
Default is MarkdownV2.Disable preview of web links in the sent message.
Default is false.Send message silently.
Default is true.

    Params:
        
        token 
        - (Required)
Telegram bot token.
        
        channel 
        - (Required)
Telegram channel ID.
        
        text 
        - (Required)
Message text.
        
        url 
        - URL of the Telegram bot endpoint. Default is https://api.telegram.org/bot.
        
        parseMode 
        - Parse mode
of the message text.
Default is MarkdownV2.
        
        disableWebPagePreview 
        - Disable preview of web links in the sent message.
Default is false.
        
        silent 
        - Send message silently.
Default is true.
        
    """
    name = "message"
    package="telegram"

    def __init__(self, token, channel, text, url=None, parseMode=None, disableWebPagePreview=None, silent=None, ):
            super().__init__(token=token, channel=channel, text=text, url=url, parseMode=parseMode, disableWebPagePreview=disableWebPagePreview, silent=silent, )