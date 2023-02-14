from flux_query_builder.functions.base import FluxQueryFunction

class WideTo(FluxQueryFunction):
    """influxdb.wideTo() writes wide data to an InfluxDB 2.x or InfluxDB Cloud bucket.
Wide data is pivoted in that its fields are represented as columns making the table wider.If using the from() to query data from InfluxDB, use pivot() to transform
data into the structure experimental.to() expects.Name of the bucket to write to.
bucket and bucketID are mutually exclusive.String-encoded bucket ID to to write to.
bucket and bucketID are mutually exclusive.URL of the InfluxDB instance to write to.See InfluxDB Cloud regions
or InfluxDB OSS URLs.
host is required when writing to a remote InfluxDB instance.
If specified, token is also required.Organization name.
org and orgID are mutually exclusive.String-encoded organization ID to query.
org and orgID are mutually exclusive.InfluxDB API token.InfluxDB 1.x or Enterprise: If authentication is disabled, provide an
empty string (""). If authentication is enabled, provide your InfluxDB
username and password using the <username>:<password> syntax.
token is required when writing to another organization or when host
is specified.Input data. Default is piped-forward data (<-).

    Params:
        
        bucket 
        - Name of the bucket to write to.
bucket and bucketID are mutually exclusive.
        
        bucketID 
        - String-encoded bucket ID to to write to.
bucket and bucketID are mutually exclusive.
        
        host 
        - URL of the InfluxDB instance to write to.See InfluxDB Cloud regions
or InfluxDB OSS URLs.
host is required when writing to a remote InfluxDB instance.
If specified, token is also required.
        
        org 
        - Organization name.
org and orgID are mutually exclusive.
        
        orgID 
        - String-encoded organization ID to query.
org and orgID are mutually exclusive.
        
        token 
        - InfluxDB API token.InfluxDB 1.x or Enterprise: If authentication is disabled, provide an
empty string (""). If authentication is enabled, provide your InfluxDB
username and password using the <username>:<password> syntax.
token is required when writing to another organization or when host
is specified.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "wideTo"
    package="influxdb"

    def __init__(self, bucket=None, bucketID=None, host=None, org=None, orgID=None, token=None, tables=None, ):
            super().__init__(bucket=bucket, bucketID=bucketID, host=host, org=org, orgID=orgID, token=token, tables=tables, )