from flux_query_builder.functions.base import FluxQueryFunction

class Get(FluxQueryFunction):
    """http.get() submits an HTTP GET request to the specified URL and returns the HTTP
status code, response body, and response headers.http.get() returns a record with the following properties:(Required)
URL to send the GET request to.Headers to include with the GET request.Timeout for the GET request. Default is 30s.

    Params:
        
        url 
        - (Required)
URL to send the GET request to.
        
        headers 
        - Headers to include with the GET request.
        
        timeout 
        - Timeout for the GET request. Default is 30s.
        
    """
    name = "get"
    package="http"

    def __init__(self, url, headers=None, timeout=None, ):
            super().__init__(url=url, headers=headers, timeout=timeout, )