from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """http.endpoint() iterates over input data and sends a single POST request per input row to
a specficied URL.This function is designed to be used with monitor.notify().http.endpoint() outputs a function that requires a mapFn parameter.
mapFn is the function that builds the record used to generate the POST request.
It accepts a table row (r) and returns a record that must include the
following properties:For information about properties, see http.post.(Required)
URL to send the POST reqeust to.

    Params:
        
        url 
        - (Required)
URL to send the POST reqeust to.
        
    """
    name = "endpoint"
    package="http"

    def __init__(self, url, ):
            super().__init__(url=url, )