from flux_query_builder.functions.base import FluxQueryFunction

class FromFunction(FluxQueryFunction):
    """iox.from() reads from the selected bucket and measurement in an IOx storage node.This function creates a source that reads data from IOx. Output data is
“pivoted” on the time column and includes columns for each returned
tag and field per time value.(Required)
IOx bucket to read data from.(Required)
Measurement to read data from.

    Params:
        
        bucket 
        - (Required)
IOx bucket to read data from.
        
        measurement 
        - (Required)
Measurement to read data from.
        
    """
    def __init__(self, bucket, measurement, ):
            super().__init__("", bucket=bucket, measurement=measurement, )