from flux_query_builder.functions.base import FluxQueryFunction

class NumericBool(FluxQueryFunction):
    """sampledata.numericBool() returns a sample data set with numeric (integer) boolean values.Include null values in the returned dataset.
Default is false.

    Params:
        
        includeNull 
        - Include null values in the returned dataset.
Default is false.
        
    """
    name = "numericBool"
    package="sampledata"

    def __init__(self, includeNull=None, ):
            super().__init__(includeNull=includeNull, )