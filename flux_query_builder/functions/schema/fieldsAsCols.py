from flux_query_builder.functions.base import FluxQueryFunction

class FieldsAsCols(FluxQueryFunction):
    """schema.fieldsAsCols() is a special application of pivot() that pivots input data
on _field and _time columns to align fields within each input table that
have the same timestamp.Input data. Default is piped-forward data (<-).

    Params:
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "fieldsAsCols"
    package="schema"

    def __init__(self, tables=None, ):
            super().__init__(tables=tables, )