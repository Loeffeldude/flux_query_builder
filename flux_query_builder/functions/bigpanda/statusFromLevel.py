from flux_query_builder.functions.base import FluxQueryFunction

class StatusFromLevel(FluxQueryFunction):
    """bigpanda.statusFromLevel() converts an alert level to a BigPanda status.BigPanda accepts one of ok, warning, or critical,.(Required)
Alert level.Use map() to iterate over rows in a stream of tables and convert alert levels to Big Panda statuses.

    Params:
        
        level 
        - (Required)
Alert level.
        
    """
    name = "statusFromLevel"
    package="bigpanda"

    def __init__(self, level, ):
            super().__init__(level=level, )