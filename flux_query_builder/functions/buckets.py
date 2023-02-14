from flux_query_builder.functions.base import FluxQueryFunction

class Buckets(FluxQueryFunction):
    """buckets() returns a list of buckets in the specified organization.Organization name. Default is the current organization.org and orgID are mutually exclusive.Organization ID. Default is the ID of the current organization.org and orgID are mutually exclusive.URL of the InfluxDB instance.See InfluxDB Cloud regions
or InfluxDB OSS URLs.
host is required when org or orgID are specified.InfluxDB API token.token is required when host, org, or orgID` are specified.

    Params:
        
        org 
        - Organization name. Default is the current organization.org and orgID are mutually exclusive.
        
        orgID 
        - Organization ID. Default is the ID of the current organization.org and orgID are mutually exclusive.
        
        host 
        - URL of the InfluxDB instance.See InfluxDB Cloud regions
or InfluxDB OSS URLs.
host is required when org or orgID are specified.
        
        token 
        - InfluxDB API token.token is required when host, org, or orgID` are specified.
        
    """
    name = "buckets"
    package=None

    def __init__(self, org=None, orgID=None, host=None, token=None, ):
            super().__init__(org=org, orgID=orgID, host=host, token=token, )