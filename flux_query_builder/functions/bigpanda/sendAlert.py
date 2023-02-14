from flux_query_builder.functions.base import FluxQueryFunction

class SendAlert(FluxQueryFunction):
    """bigpanda.sendAlert() sends an alert to BigPanda.(Required)
BigPanda alerts API URL.
Default is the value of the bigpanda.defaultURL option.(Required)
BigPanda API Authorization token (API key).(Required)
BigPanda App Key.(Required)
BigPanda alert status.Supported statuses:(Required)
Additional alert parameters to send to the BigPanda alert API.

    Params:
        
        url 
        - (Required)
BigPanda alerts API URL.
Default is the value of the bigpanda.defaultURL option.
        
        token 
        - (Required)
BigPanda API Authorization token (API key).
        
        appKey 
        - (Required)
BigPanda App Key.
        
        status 
        - (Required)
BigPanda alert status.Supported statuses:
        
        rec 
        - (Required)
Additional alert parameters to send to the BigPanda alert API.
        
    """
    name = "sendAlert"
    package="bigpanda"

    def __init__(self, url, token, appKey, status, rec, ):
            super().__init__(url=url, token=token, appKey=appKey, status=status, rec=rec, )