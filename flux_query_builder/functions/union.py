from flux_query_builder.functions.base import FluxQueryFunction

class Union(FluxQueryFunction):
    """union() merges two or more input streams into a single output stream.The output schemas of union() is the union of all input schemas.
union() does not preserve the sort order of the rows within tables.
Use sort() if you need a specific sort order.union() does not modify data in rows, but unions separate streams of tables
into a single stream of tables and groups rows of data based on existing group keys.
join() creates new rows based on common values in one or more specified columns.
Output rows also contain the differing values from each of the joined streams.(Required)
List of two or more streams of tables to union together.

    Params:
        
        tables 
        - (Required)
List of two or more streams of tables to union together.
        
    """
    name = "union"
    package=None

    def __init__(self, tables, ):
            super().__init__(tables=tables, )