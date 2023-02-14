from flux_query_builder.functions.base import FluxQueryFunction

class Query_range(FluxQueryFunction):
    """logql.query_range() queries data from a specified LogQL query within given time bounds,
filters data by query, timerange, and optional limit expressions.
All values are returned as string values (using raw mode in csv.from)LogQL/qryn URL and port. Default is http://qryn:3100.LogQL query_range API path.Query limit. Default is 100.(Required)
LogQL query to execute.Earliest time to include in results. Default is -1h.Results include points that match the specified start time.
Use a relative duration or absolute time.
For example, -1h or 2022-01-01T22:00:00.801064Z.Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration or absolute time.
For example, -1h or 2022-01-01T22:00:00.801064Z.Query resolution step width in seconds. Default is 10.Only applies to query types which produce a matrix response.Optional Loki organization ID for partitioning. Default is "".

    Params:
        
        query 
        - (Required)
LogQL query to execute.
        
        url 
        - LogQL/qryn URL and port. Default is http://qryn:3100.
        
        path 
        - LogQL query_range API path.
        
        limit 
        - Query limit. Default is 100.
        
        start 
        - Earliest time to include in results. Default is -1h.Results include points that match the specified start time.
Use a relative duration or absolute time.
For example, -1h or 2022-01-01T22:00:00.801064Z.
        
        end 
        - Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration or absolute time.
For example, -1h or 2022-01-01T22:00:00.801064Z.
        
        step 
        - Query resolution step width in seconds. Default is 10.Only applies to query types which produce a matrix response.
        
        orgid 
        - Optional Loki organization ID for partitioning. Default is "".
        
    """
    name = "query_range"
    package="logql"

    def __init__(self, query, url=None, path=None, limit=None, start=None, end=None, step=None, orgid=None, ):
            super().__init__(query=query, url=url, path=path, limit=limit, start=start, end=end, step=step, orgid=orgid, )