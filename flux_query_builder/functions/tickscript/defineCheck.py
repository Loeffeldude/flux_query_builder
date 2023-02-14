from flux_query_builder.functions.base import FluxQueryFunction

class DefineCheck(FluxQueryFunction):
    """tickscript.defineCheck() creates custom check data required by alert() and deadman().(Required)
InfluxDB check ID.(Required)
InfluxDB check name.InfluxDB check type. Default is custom.Valid values:

    Params:
        
        id 
        - (Required)
InfluxDB check ID.
        
        name 
        - (Required)
InfluxDB check name.
        
        type 
        - InfluxDB check type. Default is custom.Valid values:
        
    """
    name = "defineCheck"
    package="tickscript"

    def __init__(self, id, name, type=None, ):
            super().__init__(id=id, name=name, type=type, )