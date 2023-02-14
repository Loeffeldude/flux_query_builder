from flux_query_builder.functions.base import FluxQueryFunction

class Message(FluxQueryFunction):
    """teams.message() sends a single message to a Microsoft Teams channel using an
incoming webhook.(Required)
Incoming webhook URL.(Required)
Message card title.(Required)
Message card text.Message card summary.
Default is "".If no summary is provided, Flux generates the summary from the message text.

    Params:
        
        url 
        - (Required)
Incoming webhook URL.
        
        title 
        - (Required)
Message card title.
        
        text 
        - (Required)
Message card text.
        
        summary 
        - Message card summary.
Default is "".If no summary is provided, Flux generates the summary from the message text.
        
    """
    name = "message"
    package="teams"

    def __init__(self, url, title, text, summary=None, ):
            super().__init__(url=url, title=title, text=text, summary=summary, )