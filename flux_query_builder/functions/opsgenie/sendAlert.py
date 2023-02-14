from flux_query_builder.functions.base import FluxQueryFunction

class SendAlert(FluxQueryFunction):
    """opsgenie.sendAlert() sends an alert message to Opsgenie.Opsgenie API URL. Defaults to https://api.opsgenie.com/v2/alerts.(Required)
(Required) Opsgenie API authorization key.(Required)
(Required) Alert message text.
130 characters or less.Opsgenie alias usee to de-deduplicate alerts.
250 characters or less.
Defaults to message.Alert description. 15000 characters or less.Opsgenie alert priority.Valid values include:List of responder teams or users.
Use the user: prefix for users and teams: prefix for teams.Alert tags.Alert entity used to specify the alert domain.List of actions available for the alert.Additional alert details. Must be a JSON-encoded map of key-value string pairs.List of teams and users the alert will be visible to without sending notifications.
Use the user: prefix for users and teams: prefix for teams.

    Params:
        
        apiKey 
        - (Required)
(Required) Opsgenie API authorization key.
        
        message 
        - (Required)
(Required) Alert message text.
130 characters or less.
        
        url 
        - Opsgenie API URL. Defaults to https://api.opsgenie.com/v2/alerts.
        
        alias 
        - Opsgenie alias usee to de-deduplicate alerts.
250 characters or less.
Defaults to message.
        
        description 
        - Alert description. 15000 characters or less.
        
        priority 
        - Opsgenie alert priority.Valid values include:
        
        responders 
        - List of responder teams or users.
Use the user: prefix for users and teams: prefix for teams.
        
        tags 
        - Alert tags.
        
        entity 
        - Alert entity used to specify the alert domain.
        
        actions 
        - List of actions available for the alert.
        
        details 
        - Additional alert details. Must be a JSON-encoded map of key-value string pairs.
        
        visibleTo 
        - List of teams and users the alert will be visible to without sending notifications.
Use the user: prefix for users and teams: prefix for teams.
        
    """
    name = "sendAlert"
    package="opsgenie"

    def __init__(self, apiKey, message, url=None, alias=None, description=None, priority=None, responders=None, tags=None, entity=None, actions=None, details=None, visibleTo=None, ):
            super().__init__(apiKey=apiKey, message=message, url=url, alias=alias, description=description, priority=priority, responders=responders, tags=tags, entity=entity, actions=actions, details=details, visibleTo=visibleTo, )