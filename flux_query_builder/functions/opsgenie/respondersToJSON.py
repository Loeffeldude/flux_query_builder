from flux_query_builder.functions.base import FluxQueryFunction

class RespondersToJSON(FluxQueryFunction):
    """opsgenie.respondersToJSON() converts an array of Opsgenie responder strings
to a string-encoded JSON array that can be embedded in an alert message.(Required)
(Required) Array of Opsgenie responder strings.
Responder strings must begin with
user: , team: , escalation: , or schedule: .

    Params:
        
        v 
        - (Required)
(Required) Array of Opsgenie responder strings.
Responder strings must begin with
user: , team: , escalation: , or schedule: .
        
    """
    name = "respondersToJSON"
    package="opsgenie"

    def __init__(self, v, ):
            super().__init__(v=v, )