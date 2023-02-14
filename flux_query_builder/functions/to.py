from flux_query_builder.functions.base import FluxQueryFunction

class To(FluxQueryFunction):
    """to() writes data to an InfluxDB Cloud or 2.x bucket and returns the written data.to() writes data structured using the standard InfluxDB Cloud and v2.x data
structure that includes, at a minimum, the following columns:All other columns are written to InfluxDB as
tags.Note: to() drops rows with null _time values and does not write them
to InfluxDB.to() is part of the influxdata/influxdb package, but is part of the
Flux prelude and does not require an import statement or package namespace.Name of the bucket to write to.
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
is specified.Time column of the output. Default is "_time".Measurement column of the output. Default is "_measurement".Tag columns in the output. Defaults to all columns with type
string, excluding all value columns and columns identified by fieldFn.Function that maps a field key to a field value and returns a record.
Default is (r) => ({ [r._field]: r._value }).Input data. Default is piped-forward data (<-).The example above produces the following line protocol and sends it to the
InfluxDB /api/v2/write endpoint:The example above produces the following line protocol and sends it to the
InfluxDB /api/v2/write endpoint:The example below does the following:

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
        
        timeColumn 
        - Time column of the output. Default is "_time".
        
        measurementColumn 
        - Measurement column of the output. Default is "_measurement".
        
        tagColumns 
        - Tag columns in the output. Defaults to all columns with type
string, excluding all value columns and columns identified by fieldFn.
        
        fieldFn 
        - Function that maps a field key to a field value and returns a record.
Default is (r) => ({ [r._field]: r._value }).
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "to"
    package=None

    def __init__(self, bucket=None, bucketID=None, host=None, org=None, orgID=None, token=None, timeColumn=None, measurementColumn=None, tagColumns=None, fieldFn=None, tables=None, ):
            super().__init__(bucket=bucket, bucketID=bucketID, host=host, org=org, orgID=orgID, token=token, timeColumn=timeColumn, measurementColumn=measurementColumn, tagColumns=tagColumns, fieldFn=fieldFn, tables=tables, )