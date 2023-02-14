from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """usage.from() returns usage data from an InfluxDB Cloud organization.(Required)
Earliest time to include in results.(Required)
Latest time to include in results.InfluxDB Cloud region URL.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).InfluxDB Cloud organization ID. Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).InfluxDB Cloud API token.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).Return raw, high resolution usage data instead of downsampled usage data.
Default is false.usage.from() can query the following time ranges:The following query returns query counts for the following query endpoints:The following query compares the amount of data written to and queried from your
InfluxDB Cloud organization to your organization’s rate limits.
It appends a limitReached column to each row that indicates if your rate
limit was exceeded.

    Params:
        
        start 
        - (Required)
Earliest time to include in results.
        
        stop 
        - (Required)
Latest time to include in results.
        
        host 
        - InfluxDB Cloud region URL.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
        orgID 
        - InfluxDB Cloud organization ID. Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
        token 
        - InfluxDB Cloud API token.
Default is "".(Required if executed outside of your InfluxDB Cloud organization or region).
        
        raw 
        - Return raw, high resolution usage data instead of downsampled usage data.
Default is false.usage.from() can query the following time ranges:
        
    """
    name = "from"
    package="usage"

    def __init__(self, start, stop, host=None, orgID=None, token=None, raw=None, ):
            super().__init__(start=start, stop=stop, host=host, orgID=orgID, token=token, raw=raw, )