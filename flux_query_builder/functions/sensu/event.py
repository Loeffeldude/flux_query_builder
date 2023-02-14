from flux_query_builder.functions.base import FluxQueryFunction

class Event(FluxQueryFunction):
    """sensu.event() sends a single event to the Sensu Events API.(Required)
Base URL of Sensu API
without a trailing slash.Example: http://localhost:8080(Required)
Sensu API Key.(Required)
Check name.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.(Required)
Event text.Mapped to output in the Sensu Events API request.Sensu handlers to execute. Default is [].Event status code that indicates state.
Default is 0.Event state.
Default is "passing" for 0 status and "failing" for other statuses.Accepted values:Sensu namespace.
Default is "default".Event source.
Default is influxdb.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.

    Params:
        
        url 
        - (Required)
Base URL of Sensu API
without a trailing slash.Example: http://localhost:8080
        
        apiKey 
        - (Required)
Sensu API Key.
        
        checkName 
        - (Required)
Check name.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.
        
        text 
        - (Required)
Event text.Mapped to output in the Sensu Events API request.
        
        handlers 
        - Sensu handlers to execute. Default is [].
        
        status 
        - Event status code that indicates state.
Default is 0.
        
        state 
        - Event state.
Default is "passing" for 0 status and "failing" for other statuses.Accepted values:
        
        namespace 
        - Sensu namespace.
Default is "default".
        
        entityName 
        - Event source.
Default is influxdb.Use alphanumeric characters, underscores (_), periods (.), and hyphens (-).
All other characters are replaced with an underscore.
        
    """
    name = "event"
    package="sensu"

    def __init__(self, url, apiKey, checkName, text, handlers=None, status=None, state=None, namespace=None, entityName=None, ):
            super().__init__(url=url, apiKey=apiKey, checkName=checkName, text=text, handlers=handlers, status=status, state=state, namespace=namespace, entityName=entityName, )