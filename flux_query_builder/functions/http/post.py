from flux_query_builder.functions.base import FluxQueryFunction

class Post(FluxQueryFunction):
    """http.post() sends an HTTP POST request to the specified URL with headers and data
and returns the HTTP status code.(Required)
URL to send the POST request to.Headers to include with the POST request.Header keys with special characters:
Wrap header keys that contain special characters in double quotes ("").Data body to include with the POST request.

    Params:
        
        url 
        - (Required)
URL to send the POST request to.
        
        headers 
        - Headers to include with the POST request.Header keys with special characters:
Wrap header keys that contain special characters in double quotes ("").
        
        data 
        - Data body to include with the POST request.
        
    """
    name = "post"
    package="http"

    def __init__(self, url, headers=None, data=None, ):
            super().__init__(url=url, headers=headers, data=data, )