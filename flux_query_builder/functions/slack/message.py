from flux_query_builder.functions.base import FluxQueryFunction

class Message(FluxQueryFunction):
    """slack.message() sends a single message to a Slack channel and returns the HTTP
response code of the request.The function works with either with the chat.postMessage API or with a Slack webhook.Slack API URL.
Default is https://slack.com/api/chat.postMessage.If using the Slack webhook API, this URL is provided in the Slack webhook setup process.Slack API token. Default is "".If using the Slack Webhook API, a token is not required.(Required)
Slack channel or user to send the message to.(Required)
Message text.(Required)
Slack message color.Valid values:

    Params:
        
        channel 
        - (Required)
Slack channel or user to send the message to.
        
        text 
        - (Required)
Message text.
        
        color 
        - (Required)
Slack message color.Valid values:
        
        url 
        - Slack API URL.
Default is https://slack.com/api/chat.postMessage.If using the Slack webhook API, this URL is provided in the Slack webhook setup process.
        
        token 
        - Slack API token. Default is "".If using the Slack Webhook API, a token is not required.
        
    """
    name = "message"
    package="slack"

    def __init__(self, channel, text, color, url=None, token=None, ):
            super().__init__(channel=channel, text=text, color=color, url=url, token=token, )