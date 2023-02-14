from flux_query_builder.functions.base import FluxQueryFunction

class Alert(FluxQueryFunction):
    """alerta.alert() sends an alert to Alerta.(Required)
(Required) Alerta URL.(Required)
(Required) Alerta API key.(Required)
(Required) Resource associated with the alert.(Required)
(Required) Event name.Alerta environment. Valid values: “Production”, “Development” or empty string (default).(Required)
(Required) Event severity. See Alerta severities.List of affected services. Default is [].Alerta event group. Default is "".Event value. Default is "".Alerta text description. Default is "".List of event tags. Default is [].(Required)
(Required) Alert attributes.monitoring component.Event type. Default is "".time alert was generated. Default is now().

    Params:
        
        url 
        - (Required)
(Required) Alerta URL.
        
        apiKey 
        - (Required)
(Required) Alerta API key.
        
        resource 
        - (Required)
(Required) Resource associated with the alert.
        
        event 
        - (Required)
(Required) Event name.
        
        severity 
        - (Required)
(Required) Event severity. See Alerta severities.
        
        attributes 
        - (Required)
(Required) Alert attributes.
        
        environment 
        - Alerta environment. Valid values: “Production”, “Development” or empty string (default).
        
        service 
        - List of affected services. Default is [].
        
        group 
        - Alerta event group. Default is "".
        
        value 
        - Event value. Default is "".
        
        text 
        - Alerta text description. Default is "".
        
        tags 
        - List of event tags. Default is [].
        
        origin 
        - monitoring component.
        
        type 
        - Event type. Default is "".
        
        timestamp 
        - time alert was generated. Default is now().
        
    """
    name = "alert"
    package="alerta"

    def __init__(self, url, apiKey, resource, event, severity, attributes, environment=None, service=None, group=None, value=None, text=None, tags=None, origin=None, type=None, timestamp=None, ):
            super().__init__(url=url, apiKey=apiKey, resource=resource, event=event, severity=severity, attributes=attributes, environment=environment, service=service, group=group, value=value, text=text, tags=tags, origin=origin, type=type, timestamp=timestamp, )