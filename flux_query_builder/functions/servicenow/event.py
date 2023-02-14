from flux_query_builder.functions.base import FluxQueryFunction

class Event(FluxQueryFunction):
    """servicenow.event() sends an event to ServiceNow.ServiceNow Event API fields are described in
ServiceNow Create Event documentation.(Required)
ServiceNow web service URL.(Required)
ServiceNow username to use for HTTP BASIC authentication.(Required)
ServiceNow password to use for HTTP BASIC authentication.(Required)
Event description.(Required)
Severity of the event.Supported values:Source name. Default is "Flux".Node name or IP address related to the event.
Default is an empty string ("").Metric type related to the event (for example, CPU).
Default is an empty string ("").Resource related to the event (for example, CPU-1).
Default is an empty string ("").Metric name related to the event (for example, usage_idle).
Default is an empty string ("").Unique identifier of the event (for example, the InfluxDB alert ID).
Default is an empty string ("").
If an empty string, ServiceNow generates a value.Additional information to include with the event.

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
        
        description 
        - (Required)
Event description.
        
        severity 
        - (Required)
Severity of the event.Supported values:
        
        source 
        - Source name. Default is "Flux".
        
        node 
        - Node name or IP address related to the event.
Default is an empty string ("").
        
        metricType 
        - Metric type related to the event (for example, CPU).
Default is an empty string ("").
        
        resource 
        - Resource related to the event (for example, CPU-1).
Default is an empty string ("").
        
        metricName 
        - Metric name related to the event (for example, usage_idle).
Default is an empty string ("").
        
        messageKey 
        - Unique identifier of the event (for example, the InfluxDB alert ID).
Default is an empty string ("").
If an empty string, ServiceNow generates a value.
        
        additionalInfo 
        - Additional information to include with the event.
        
    """
    name = "event"
    package="servicenow"

    def __init__(self, url, username, password, description, severity, source=None, node=None, metricType=None, resource=None, metricName=None, messageKey=None, additionalInfo=None, ):
            super().__init__(url=url, username=username, password=password, description=description, severity=severity, source=source, node=node, metricType=metricType, resource=resource, metricName=metricName, messageKey=messageKey, additionalInfo=additionalInfo, )