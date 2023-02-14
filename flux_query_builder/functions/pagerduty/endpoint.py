from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """pagerduty.endpoint() returns a function that sends a message to PagerDuty that includes output data.pagerduty.endpoint() is a factory function that outputs another function.
The output function requires a mapFn parameter.Function that builds the record used to generate the POST request.
Requires an r parameter.mapFn accepts a table row (r) and returns a record that must include the
following properties:PagerDuty v2 Events API URL.Default is https://events.pagerduty.com/v2/enqueue.

    Params:
        
        url 
        - PagerDuty v2 Events API URL.Default is https://events.pagerduty.com/v2/enqueue.
        
    """
    name = "endpoint"
    package="pagerduty"

    def __init__(self, url=None, ):
            super().__init__(url=url, )