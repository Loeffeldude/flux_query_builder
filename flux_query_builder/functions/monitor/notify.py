from flux_query_builder.functions.base import FluxQueryFunction

class Notify(FluxQueryFunction):
    """monitor.notify() sends a notification to an endpoint and logs it in the notifications
measurement in the _monitoring bucket.(Required)
A function that constructs and sends the notification to an endpoint.(Required)
Notification data to append to the output.This data specifies which notification rule and notification endpoint to
associate with the sent notification.
The data record must contain the following properties:Input data. Default is piped-forward data (<-).

    Params:
        
        endpoint 
        - (Required)
A function that constructs and sends the notification to an endpoint.
        
        data 
        - (Required)
Notification data to append to the output.This data specifies which notification rule and notification endpoint to
associate with the sent notification.
The data record must contain the following properties:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "notify"
    package="monitor"

    def __init__(self, endpoint, data, tables=None, ):
            super().__init__(endpoint=endpoint, data=data, tables=tables, )