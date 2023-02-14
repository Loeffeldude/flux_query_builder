from flux_query_builder.functions.base import FluxQueryFunction

class Databases(FluxQueryFunction):
    """v1.databases() returns a list of databases in an InfluxDB 1.x (1.7+) instance.Output includes the following columns:Organization name.Organization ID.InfluxDB URL. Default is http://localhost:8086.InfluxDB API token.

    Params:
        
        org 
        - Organization name.
        
        orgID 
        - Organization ID.
        
        host 
        - InfluxDB URL. Default is http://localhost:8086.
        
        token 
        - InfluxDB API token.
        
    """
    name = "databases"
    package="v1"

    def __init__(self, org=None, orgID=None, host=None, token=None, ):
            super().__init__(org=org, orgID=orgID, host=host, token=token, )