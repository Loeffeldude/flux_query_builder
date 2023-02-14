from flux_query_builder.functions.base import FluxQueryFunction

class SendEvent(FluxQueryFunction):
    """pagerduty.sendEvent() sends an event to PagerDuty and returns the HTTP response code of the request.PagerDuty endpoint URL.Default is https://events.pagerduty.com/v2/enqueue.(Required)
Routing key generated from your PagerDuty integration.(Required)
Name of the client sending the alert.(Required)
URL of the client sending the alert.(Required)
Per-alert ID that acts as deduplication key and allows you to
acknowledge or change the severity of previous messages.
Supports a maximum of 255 characters.(Required)
Class or type of the event.Classes are user-defined.
For example, ping failure or cpu load.(Required)
Logical grouping used by PagerDuty.Groups are user-defined.
For example, app-stack.(Required)
Severity of the event.Valid values:(Required)
Event type to send to PagerDuty.Valid values:(Required)
Unique location of the affected system.
For example, the hostname or fully qualified domain name (FQDN).Component responsible for the event.(Required)
Brief text summary of the event used as the summaries or titles of associated alerts.
The maximum permitted length is 1024 characters.(Required)
Time the detected event occurred in RFC3339nano format.Record with additional details about the event.

    Params:
        
        routingKey 
        - (Required)
Routing key generated from your PagerDuty integration.
        
        client 
        - (Required)
Name of the client sending the alert.
        
        clientURL 
        - (Required)
URL of the client sending the alert.
        
        dedupKey 
        - (Required)
Per-alert ID that acts as deduplication key and allows you to
acknowledge or change the severity of previous messages.
Supports a maximum of 255 characters.
        
        class_ 
        - (Required)
Class or type of the event.Classes are user-defined.
For example, ping failure or cpu load.
        
        group 
        - (Required)
Logical grouping used by PagerDuty.Groups are user-defined.
For example, app-stack.
        
        severity 
        - (Required)
Severity of the event.Valid values:
        
        eventAction 
        - (Required)
Event type to send to PagerDuty.Valid values:
        
        source 
        - (Required)
Unique location of the affected system.
For example, the hostname or fully qualified domain name (FQDN).
        
        summary 
        - (Required)
Brief text summary of the event used as the summaries or titles of associated alerts.
The maximum permitted length is 1024 characters.
        
        timestamp 
        - (Required)
Time the detected event occurred in RFC3339nano format.
        
        pagerdutyURL 
        - PagerDuty endpoint URL.Default is https://events.pagerduty.com/v2/enqueue.
        
        component 
        - Component responsible for the event.
        
        customDetails 
        - Record with additional details about the event.
        
    """
    name = "sendEvent"
    package="pagerduty"

    def __init__(self, routingKey, client, clientURL, dedupKey, class_, group, severity, eventAction, source, summary, timestamp, pagerdutyURL=None, component=None, customDetails=None, ):
            super().__init__(routingKey=routingKey, client=client, clientURL=clientURL, dedupKey=dedupKey, class_=class_, group=group, severity=severity, eventAction=eventAction, source=source, summary=summary, timestamp=timestamp, pagerdutyURL=pagerdutyURL, component=component, customDetails=customDetails, )