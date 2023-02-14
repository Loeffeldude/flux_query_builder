from flux_query_builder.functions.base import FluxQueryFunction

class Int(FluxQueryFunction):
    """sampledata.int() returns a sample data set with integer values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "int"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )