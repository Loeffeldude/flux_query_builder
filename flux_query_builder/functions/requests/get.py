from flux_query_builder.functions.base import FluxQueryFunction

class Get(FluxQueryFunction):
    """requests.get() makes a http GET request. This identical to calling request.do(method: "GET", ...).(Required)
URL to request. This should not include any query parameters.Set of key value pairs to add to the URL as query parameters.
Query parameters will be URL encoded.
All values for a key will be appended to the query.Set of key values pairs to include on the request.Data to send with the request.Set of options to control how the request should be performed.

    Params:
        
        url 
        - (Required)
URL to request. This should not include any query parameters.
        
        params 
        - Set of key value pairs to add to the URL as query parameters.
Query parameters will be URL encoded.
All values for a key will be appended to the query.
        
        headers 
        - Set of key values pairs to include on the request.
        
        body 
        - Data to send with the request.
        
        config 
        - Set of options to control how the request should be performed.
        
    """
    name = "get"
    package="requests"

    def __init__(self, url, params=None, headers=None, body=None, config=None, ):
            super().__init__(url=url, params=params, headers=headers, body=body, config=config, )