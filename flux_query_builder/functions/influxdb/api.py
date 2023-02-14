from flux_query_builder.functions.base import FluxQueryFunction

class Api(FluxQueryFunction):
    """influxdb.api() submits an HTTP request to the specified InfluxDB API path and returns a
record containing the HTTP status code, response headers, and the response body.Note: influxdb.api() uses the authorization of the specified token or, if executed
from the InfluxDB UI, the authorization of the InfluxDB user that invokes the script.
Authorization permissions and limits apply to each request.influxdb.api() returns a record with the following properties:(Required)
HTTP request method.(Required)
InfluxDB API path.InfluxDB host URL (Required when executed outside of InfluxDB).
Default is "".InfluxDB API token
(Required when executed outside of InfluxDB).
Default is "".HTTP request headers.URL query parameters.HTTP request timeout. Default is 30s.HTTP request body as bytes.

    Params:
        
        method 
        - (Required)
HTTP request method.
        
        path 
        - (Required)
InfluxDB API path.
        
        host 
        - InfluxDB host URL (Required when executed outside of InfluxDB).
Default is "".
        
        token 
        - InfluxDB API token
(Required when executed outside of InfluxDB).
Default is "".
        
        headers 
        - HTTP request headers.
        
        query 
        - URL query parameters.
        
        timeout 
        - HTTP request timeout. Default is 30s.
        
        body 
        - HTTP request body as bytes.
        
    """
    name = "api"
    package="influxdb"

    def __init__(self, method, path, host=None, token=None, headers=None, query=None, timeout=None, body=None, ):
            super().__init__(method=method, path=path, host=host, token=token, headers=headers, query=query, timeout=timeout, body=body, )