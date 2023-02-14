from flux_query_builder.functions.base import FluxQueryFunction

class Query(FluxQueryFunction):
    """clickhouse.query() queries data from ClickHouse using specified parameters.ClickHouse HTTP API URL. Default is http://127.0.0.1:8123.(Required)
ClickHouse query to execute.Query rows limit. Defaults is 100.Request remote CORS headers. Defaults is 1.Query bytes limit. Default is 10000000.Query format. Default is CSVWithNames.For information about available formats, see ClickHouse formats.

    Params:
        
        query 
        - (Required)
ClickHouse query to execute.
        
        url 
        - ClickHouse HTTP API URL. Default is http://127.0.0.1:8123.
        
        limit 
        - Query rows limit. Defaults is 100.
        
        cors 
        - Request remote CORS headers. Defaults is 1.
        
        max_bytes 
        - Query bytes limit. Default is 10000000.
        
        format 
        - Query format. Default is CSVWithNames.For information about available formats, see ClickHouse formats.
        
    """
    name = "query"
    package="clickhouse"

    def __init__(self, query, url=None, limit=None, cors=None, max_bytes=None, format=None, ):
            super().__init__(query=query, url=url, limit=limit, cors=cors, max_bytes=max_bytes, format=format, )