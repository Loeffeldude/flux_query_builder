from flux_query_builder.functions.base import FluxQueryFunction

class Cardinality(FluxQueryFunction):
    """influxdb.cardinality() returns the series cardinality of data stored in InfluxDB.Bucket to query cardinality from.String-encoded bucket ID to query cardinality from.Organization name.String-encoded organization ID.URL of the InfluxDB instance to query.See InfluxDB Cloud regions
or InfluxDB OSS URLs.InfluxDB API token.(Required)
Earliest time to include when calculating cardinality.The cardinality calculation includes points that match the specified start time.
Use a relative duration or absolute time. For example, -1h or 2019-08-28T22:00:00Z.
Durations are relative to now().Latest time to include when calculating cardinality.The cardinality calculation excludes points that match the specified start time.
Use a relative duration or absolute time. For example, -1h or 2019-08-28T22:00:00Z.
Durations are relative to now(). Default is now().Predicate function that filters records.
Default is (r) => true.

    Params:
        
        start 
        - (Required)
Earliest time to include when calculating cardinality.The cardinality calculation includes points that match the specified start time.
Use a relative duration or absolute time. For example, -1h or 2019-08-28T22:00:00Z.
Durations are relative to now().
        
        bucket 
        - Bucket to query cardinality from.
        
        bucketID 
        - String-encoded bucket ID to query cardinality from.
        
        org 
        - Organization name.
        
        orgID 
        - String-encoded organization ID.
        
        host 
        - URL of the InfluxDB instance to query.See InfluxDB Cloud regions
or InfluxDB OSS URLs.
        
        token 
        - InfluxDB API token.
        
        stop 
        - Latest time to include when calculating cardinality.The cardinality calculation excludes points that match the specified start time.
Use a relative duration or absolute time. For example, -1h or 2019-08-28T22:00:00Z.
Durations are relative to now(). Default is now().
        
        predicate 
        - Predicate function that filters records.
Default is (r) => true.
        
    """
    name = "cardinality"
    package="influxdb"

    def __init__(self, start, bucket=None, bucketID=None, org=None, orgID=None, host=None, token=None, stop=None, predicate=None, ):
            super().__init__(start=start, bucket=bucket, bucketID=bucketID, org=org, orgID=orgID, host=host, token=token, stop=stop, predicate=predicate, )