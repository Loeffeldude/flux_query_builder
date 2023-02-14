from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """servicenow.endpoint() sends events to ServiceNow using data from input rows.servicenow.endpoint is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the ServiceNow API request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following properties:For more information, see servicenow.event() parameters.(Required)
ServiceNow web service URL.(Required)
ServiceNow username to use for HTTP BASIC authentication.(Required)
ServiceNow password to use for HTTP BASIC authentication.Source name. Default is "Flux".

    Params:
        
        url 
        - (Required)
ServiceNow web service URL.
        
        username 
        - (Required)
ServiceNow username to use for HTTP BASIC authentication.
        
        password 
        - (Required)
ServiceNow password to use for HTTP BASIC authentication.
        
        source 
        - Source name. Default is "Flux".
        
    """
    name = "endpoint"
    package="servicenow"

    def __init__(self, url, username, password, source=None, ):
            super().__init__(url=url, username=username, password=password, source=source, )