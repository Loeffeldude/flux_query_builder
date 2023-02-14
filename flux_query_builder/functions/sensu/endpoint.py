from flux_query_builder.functions.base import FluxQueryFunction

class Endpoint(FluxQueryFunction):
    """sensu.endpoint() sends an event
to the Sensu Events API
using data from table rows.sensu.endpoint() is a factory function that outputs another function.
The output function requires a mapFn parameter.A function that builds the object used to generate the POST request. Requires an r parameter.mapFn accepts a table row (r) and returns an object that must include the following fields:For more information, see sensu.event() parameters.(Required)
Base URL of Sensu API
without a trailing slash.
Example: http://localhost:8080.(Required)
Sensu API Key.Sensu handlers to execute.
Default is [].Sensu namespace.
Default is default.Event source.
Default is influxdb.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.

    Params:
        
        url 
        - (Required)
Base URL of Sensu API
without a trailing slash.
Example: http://localhost:8080.
        
        apiKey 
        - (Required)
Sensu API Key.
        
        handlers 
        - Sensu handlers to execute.
Default is [].
        
        namespace 
        - Sensu namespace.
Default is default.
        
        entityName 
        - Event source.
Default is influxdb.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.
        
    """
    name = "endpoint"
    package="sensu"

    def __init__(self, url, apiKey, handlers=None, namespace=None, entityName=None, ):
            super().__init__(url=url, apiKey=apiKey, handlers=handlers, namespace=namespace, entityName=entityName, )