from flux_query_builder.functions.base import FluxQueryFunction

class ActionFromSeverity(FluxQueryFunction):
    """pagerduty.actionFromSeverity() converts a severity to a PagerDuty action.(Required)
Severity to convert to a PagerDuty action.

    Params:
        
        severity 
        - (Required)
Severity to convert to a PagerDuty action.
        
    """
    name = "actionFromSeverity"
    package="pagerduty"

    def __init__(self, severity, ):
            super().__init__(severity=severity, )