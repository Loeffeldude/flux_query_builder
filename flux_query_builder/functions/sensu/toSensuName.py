from flux_query_builder.functions.base import FluxQueryFunction

class ToSensuName(FluxQueryFunction):
    """sensu.toSensuName() translates a string value to a Sensu name
by replacing non-alphanumeric characters ([a-zA-Z0-9_.-]) with underscores (_).(Required)
String to operate on.

    Params:
        
        v 
        - (Required)
String to operate on.
        
    """
    name = "toSensuName"
    package="sensu"

    def __init__(self, v, ):
            super().__init__(v=v, )