from flux_query_builder.functions.base import FluxQueryFunction

class Select(FluxQueryFunction):
    """influxdb.select() is an alternate implementation of from(),
range(), filter() and pivot() that returns pivoted query results and masks
the _measurement, _start, and _stop columns. Results are similar to those
returned by InfluxQL SELECT statements.(Required)
Name of the bucket to query.(Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().(Required)
Name of the measurement to query.List of fields to query. Default is[].Returns all fields when list is empty or unspecified.Single argument predicate function that evaluates true or false
and filters results based on tag values.
Default is (r) => true.Records are passed to the function before fields are pivoted into columns.
Records that evaluate to true are included in the output tables.
Records that evaluate to null or false are not included in the output tables.URL of the InfluxDB instance to query.See InfluxDB OSS URLs
or InfluxDB Cloud regions.Organization name.InfluxDB API token.

    Params:
        
        from_ 
        - (Required)
Name of the bucket to query.
        
        start 
        - (Required)
Earliest time to include in results.Results include points that match the specified start time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        m 
        - (Required)
Name of the measurement to query.
        
        stop 
        - Latest time to include in results. Default is now().Results exclude points that match the specified stop time.
Use a relative duration, absolute time, or integer (Unix timestamp in seconds).
For example, -1h, 2019-08-28T22:00:00Z, or 1567029600.
Durations are relative to now().
        
        fields 
        - List of fields to query. Default is[].Returns all fields when list is empty or unspecified.
        
        where 
        - Single argument predicate function that evaluates true or false
and filters results based on tag values.
Default is (r) => true.Records are passed to the function before fields are pivoted into columns.
Records that evaluate to true are included in the output tables.
Records that evaluate to null or false are not included in the output tables.
        
        host 
        - URL of the InfluxDB instance to query.See InfluxDB OSS URLs
or InfluxDB Cloud regions.
        
        org 
        - Organization name.
        
        token 
        - InfluxDB API token.
        
    """
    name = "select"
    package="influxdb"

    def __init__(self, from_, start, m, stop=None, fields=None, where=None, host=None, org=None, token=None, ):
            super().__init__(from_=from_, start=start, m=m, stop=stop, fields=fields, where=where, host=host, org=org, token=token, )