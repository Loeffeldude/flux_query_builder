from flux_query_builder.functions.base import FluxQueryFunction

class Filter(FluxQueryFunction):
    """filter() filters data based on conditions defined in a predicate function (fn).Output tables have the same schema as the corresponding input tables.(Required)
Single argument predicate function that evaluates true or false.Records representing each row are passed to the function as r.
Records that evaluate to true are included in output tables.
Records that evaluate to null or false are excluded from output tables.Action to take with empty tables. Default is drop.Supported values:Input data. Default is piped-forward data (<-).

    Params:
        
        fn 
        - (Required)
Single argument predicate function that evaluates true or false.Records representing each row are passed to the function as r.
Records that evaluate to true are included in output tables.
Records that evaluate to null or false are excluded from output tables.
        
        onEmpty 
        - Action to take with empty tables. Default is drop.Supported values:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "filter"
    package=None

    def __init__(self, fn, onEmpty=None, tables=None, ):
            super().__init__(fn=fn, onEmpty=onEmpty, tables=tables, )