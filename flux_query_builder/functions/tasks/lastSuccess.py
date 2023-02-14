from flux_query_builder.functions.base import FluxQueryFunction

class LastSuccess(FluxQueryFunction):
    """tasks.lastSuccess() returns the time of the last successful run of the InfluxDB task
or the value of the orTime parameter if the task has never successfully run.(Required)
Defualt time value returned if the task has never successfully run.

    Params:
        
        orTime 
        - (Required)
Defualt time value returned if the task has never successfully run.
        
    """
    name = "lastSuccess"
    package="tasks"

    def __init__(self, orTime, ):
            super().__init__(orTime=orTime, )