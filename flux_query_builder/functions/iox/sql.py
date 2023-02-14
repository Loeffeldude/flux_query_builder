from flux_query_builder.functions.base import FluxQueryFunction

class Sql(FluxQueryFunction):
    """iox.sql() executes an SQL query against a bucket in an IOx storage node.This function creates a source that reads data from IOx.(Required)
IOx bucket to read data from.(Required)
SQL query to execute.

    Params:
        
        bucket 
        - (Required)
IOx bucket to read data from.
        
        query 
        - (Required)
SQL query to execute.
        
    """
    name = "sql"
    package="iox"

    def __init__(self, bucket, query, ):
            super().__init__(bucket=bucket, query=query, )