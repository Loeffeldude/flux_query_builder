from flux_query_builder.functions.base import FluxQueryFunction

class ActionFromLevel(FluxQueryFunction):
    """pagerduty.actionFromLevel() converts a monitoring level to a PagerDuty action.(Required)
Monitoring level to convert to a PagerDuty action.

    Params:
        
        level 
        - (Required)
Monitoring level to convert to a PagerDuty action.
        
    """
    name = "actionFromLevel"
    package="pagerduty"

    def __init__(self, level, ):
            super().__init__(level=level, )