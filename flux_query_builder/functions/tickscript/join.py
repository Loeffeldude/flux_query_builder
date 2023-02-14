from flux_query_builder.functions.base import FluxQueryFunction

class Join(FluxQueryFunction):
    """tickscript.join() merges two input streams into a single output stream
based on specified columns with equal values and appends a new measurement name.This function is comparable to Kapacitor JoinNode.(Required)
Map of two streams to join.List of columns to join on. Default is ["_time"].(Required)
Measurement name to use in results.

    Params:
        
        tables 
        - (Required)
Map of two streams to join.
        
        measurement 
        - (Required)
Measurement name to use in results.
        
        on 
        - List of columns to join on. Default is ["_time"].
        
    """
    name = "join"
    package="tickscript"

    def __init__(self, tables, measurement, on=None, ):
            super().__init__(tables=tables, measurement=measurement, on=on, )