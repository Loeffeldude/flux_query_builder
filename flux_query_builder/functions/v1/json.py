from flux_query_builder.functions.base import FluxQueryFunction

class Json(FluxQueryFunction):
    """v1.json() parses an InfluxDB 1.x JSON result into a stream of tables.InfluxDB 1.x query results in JSON format.json and file are mutually exclusive.File path to file containing InfluxDB 1.x query results in JSON format.The path can be absolute or relative.
If relative, it is relative to the working directory of the fluxd process.
The JSON file must exist in the same file system running the fluxd process.
Note: InfluxDB OSS and InfluxDB Cloud do not support the file parameter.
Neither allow access to the underlying filesystem.

    Params:
        
        json 
        - InfluxDB 1.x query results in JSON format.json and file are mutually exclusive.
        
        file 
        - File path to file containing InfluxDB 1.x query results in JSON format.The path can be absolute or relative.
If relative, it is relative to the working directory of the fluxd process.
The JSON file must exist in the same file system running the fluxd process.
Note: InfluxDB OSS and InfluxDB Cloud do not support the file parameter.
Neither allow access to the underlying filesystem.
        
    """
    name = "json"
    package="v1"

    def __init__(self, json=None, file=None, ):
            super().__init__(json=json, file=file, )