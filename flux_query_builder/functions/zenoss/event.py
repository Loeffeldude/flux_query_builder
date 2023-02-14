from flux_query_builder.functions.base import FluxQueryFunction

class Event(FluxQueryFunction):
    """zenoss.event() sends an event to Zenoss.(Required)
Zenoss router endpoint URL.Zenoss username to use for HTTP BASIC authentication.
Default is "" (no authentication).Zenoss password to use for HTTP BASIC authentication.
Default is "" (no authentication).Zenoss cloud API key.
Default is "" (no API key).Zenoss router name.
Default is “EventsRouter”.EventsRouter method.
Default is “add_event”.Event type.
Default is “rpc”.Temporary request transaction ID.
Default is 1.Event summary.
Default is "".Related device.
Default is "".Related component.
Default is "".(Required)
Event severity level.Supported values:Event class.
Default is "".Event class key.
Default is "".Zenoss collector.
Default is "".Related message.
Default is "".

    Params:
        
        url 
        - (Required)
Zenoss router endpoint URL.
        
        severity 
        - (Required)
Event severity level.Supported values:
        
        username 
        - Zenoss username to use for HTTP BASIC authentication.
Default is "" (no authentication).
        
        password 
        - Zenoss password to use for HTTP BASIC authentication.
Default is "" (no authentication).
        
        apiKey 
        - Zenoss cloud API key.
Default is "" (no API key).
        
        action 
        - Zenoss router name.
Default is “EventsRouter”.
        
        method 
        - EventsRouter method.
Default is “add_event”.
        
        type 
        - Event type.
Default is “rpc”.
        
        tid 
        - Temporary request transaction ID.
Default is 1.
        
        summary 
        - Event summary.
Default is "".
        
        device 
        - Related device.
Default is "".
        
        component 
        - Related component.
Default is "".
        
        eventClass 
        - Event class.
Default is "".
        
        eventClassKey 
        - Event class key.
Default is "".
        
        collector 
        - Zenoss collector.
Default is "".
        
        message 
        - Related message.
Default is "".
        
    """
    name = "event"
    package="zenoss"

    def __init__(self, url, severity, username=None, password=None, apiKey=None, action=None, method=None, type=None, tid=None, summary=None, device=None, component=None, eventClass=None, eventClassKey=None, collector=None, message=None, ):
            super().__init__(url=url, severity=severity, username=username, password=password, apiKey=apiKey, action=action, method=method, type=type, tid=tid, summary=summary, device=device, component=component, eventClass=eventClass, eventClassKey=eventClassKey, collector=collector, message=message, )