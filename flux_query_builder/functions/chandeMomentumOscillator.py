from flux_query_builder.functions.base import FluxQueryFunction

class ChandeMomentumOscillator(FluxQueryFunction):
    """chandeMomentumOscillator() applies the technical momentum indicator developed
by Tushar Chande to input data.The Chande Momentum Oscillator (CMO) indicator does the following:For each input table with x rows, chandeMomentumOscillator() outputs a
table with x - n rows.(Required)
Period or number of points to use in the calculation.List of columns to operate on. Default is ["_value"].Input data. Default is piped-forward data (<-).

    Params:
        
        n 
        - (Required)
Period or number of points to use in the calculation.
        
        columns 
        - List of columns to operate on. Default is ["_value"].
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "chandeMomentumOscillator"
    package=None

    def __init__(self, n, columns=None, tables=None, ):
            super().__init__(n=n, columns=columns, tables=tables, )