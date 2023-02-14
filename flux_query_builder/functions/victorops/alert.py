from flux_query_builder.functions.base import FluxQueryFunction

class Alert(FluxQueryFunction):
    """victorops.alert() sends an alert to VictorOps.(Required)
VictorOps REST endpoint integration URL.Example: https://alert.victorops.com/integrations/generic/00000000/alert/<api_key>/<routing_key>
Replace <api_key> and <routing_key> with valid VictorOps API and routing keys.Monitoring agent name. Default is "".(Required)
VictorOps message type (alert behavior).Valid values:Incident ID. Default is "".Incident display name or summary. Default is "".Verbose incident message. Default is "".Incident start time. Default is now().

    Params:
        
        url 
        - (Required)
VictorOps REST endpoint integration URL.Example: https://alert.victorops.com/integrations/generic/00000000/alert/<api_key>/<routing_key>
Replace <api_key> and <routing_key> with valid VictorOps API and routing keys.
        
        messageType 
        - (Required)
VictorOps message type (alert behavior).Valid values:
        
        monitoringTool 
        - Monitoring agent name. Default is "".
        
        entityID 
        - Incident ID. Default is "".
        
        entityDisplayName 
        - Incident display name or summary. Default is "".
        
        stateMessage 
        - Verbose incident message. Default is "".
        
        timestamp 
        - Incident start time. Default is now().
        
    """
    name = "alert"
    package="victorops"

    def __init__(self, url, messageType, monitoringTool=None, entityID=None, entityDisplayName=None, stateMessage=None, timestamp=None, ):
            super().__init__(url=url, messageType=messageType, monitoringTool=monitoringTool, entityID=entityID, entityDisplayName=entityDisplayName, stateMessage=stateMessage, timestamp=timestamp, )