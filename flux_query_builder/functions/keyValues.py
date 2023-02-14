from flux_query_builder.functions.base import FluxQueryFunction

class KeyValues(FluxQueryFunction):
    """keyValues() returns a stream of tables with each input tables’ group key and
two columns, _key and _value, that correspond to unique column label and value
pairs for each input table.List of columns from which values are extracted.All columns must be of the same type.
Each input table must have all of the columns in the keyColumns parameter.Input data. Default is piped-forward data (<-).

    Params:
        
        keyColumns 
        - List of columns from which values are extracted.All columns must be of the same type.
Each input table must have all of the columns in the keyColumns parameter.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "keyValues"
    package=None

    def __init__(self, keyColumns=None, tables=None, ):
            super().__init__(keyColumns=keyColumns, tables=tables, )