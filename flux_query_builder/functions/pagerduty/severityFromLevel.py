from flux_query_builder.functions.base import FluxQueryFunction

class SeverityFromLevel(FluxQueryFunction):
    """pagerduty.severityFromLevel() converts an InfluxDB status level to a PagerDuty severity.(Required)
InfluxDB status level to convert to a PagerDuty severity.

    Params:
        
        level 
        - (Required)
InfluxDB status level to convert to a PagerDuty severity.
        
    """
    name = "severityFromLevel"
    package="pagerduty"

    def __init__(self, level, ):
            super().__init__(level=level, )