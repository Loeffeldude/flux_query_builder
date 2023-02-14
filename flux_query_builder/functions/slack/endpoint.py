from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """slack.endpoint() returns a function that can be used to send a message to Slack per input row.Each output row includes a _sent column that indicates if the message for
that row was sent successfully.slack.endpoint() is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the record used to generate the POST request.mapFn accepts a table row (r) and returns a record that must include the
following properties:Slack API URL. Default is https://slack.com/api/chat.postMessage.If using the Slack webhook API, this URL is provided ine Slack webhook setup process.Slack API token. Default is "".If using the Slack Webhook API, a token is not required.

    Params:
        
        url 
        - Slack API URL. Default is https://slack.com/api/chat.postMessage.If using the Slack webhook API, this URL is provided ine Slack webhook setup process.
        
        token 
        - Slack API token. Default is "".If using the Slack Webhook API, a token is not required.
        
    """
    name = "endpoint"
    package="slack"

    def __init__(self, url=None, token=None, ):
            super().__init__(url=url, token=token, )