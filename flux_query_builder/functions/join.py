from flux_query_builder.functions.base import FluxQueryFunction

class Join(FluxQueryFunction):
    """join() merges two streams of tables into a single output stream based on columns with equal values.
Null values are not considered equal when comparing column values.
The resulting schema is the union of the input schemas.
The resulting group key is the union of the input group keys.The schema and group keys of the joined output output data is the union of
the input schemas and group keys.
Columns that exist in both input streams that are not part specified as
columns to join on are renamed using the pattern <column>_<table> to
prevent ambiguity in joined tables.join() creates new rows based on common values in one or more specified columns.
Output rows also contain the differing values from each of the joined streams.
union() does not modify data in rows, but unions separate streams of tables
into a single stream of tables and groups rows of data based on existing group keys.Record containing two input streams to join.List of columns to join on.Join method. Default is inner.Supported methods:

    Params:
        
        tables 
        - Record containing two input streams to join.
        
        on 
        - List of columns to join on.
        
        method 
        - Join method. Default is inner.Supported methods:
        
    """
    name = "join"
    package=None

    def __init__(self, tables=None, on=None, method=None, ):
            super().__init__(tables=tables, on=on, method=method, )