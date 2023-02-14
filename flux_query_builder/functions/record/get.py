from flux_query_builder.functions.base import FluxQueryFunction

class Get(FluxQueryFunction):
    """record.get() returns a value from a record by key name or a default value if the key
doesn’t exist in the record.This is an interim solution for the exists operator’s limited use with
records outside of a stream of tables.
For more information, see influxdata/flux#4073.(Required)
Record to retrieve the value from.(Required)
Property key to retrieve.(Required)
Default value to return if the specified key does not exist in the record.

    Params:
        
        r 
        - (Required)
Record to retrieve the value from.
        
        key 
        - (Required)
Property key to retrieve.
        
        default 
        - (Required)
Default value to return if the specified key does not exist in the record.
        
    """
    name = "get"
    package="record"

    def __init__(self, r, key, default, ):
            super().__init__(r=r, key=key, default=default, )