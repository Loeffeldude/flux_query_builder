from flux_query_builder.functions.base import FluxQueryFunction

class Elapsed(FluxQueryFunction):
    """elapsed() returns the time between subsequent records.For each input table, elapsed() returns the same table without the first row
(because there is no previous time to derive the elapsed time from) and an
additional column containing the elapsed time.Unit of time used in the calculation. Default is 1s.Column to use to compute the elapsed time. Default is _time.Column to store elapsed times in. Default is elapsed.Input data. Default is piped-forward data (<-).

    Params:
        
        unit 
        - Unit of time used in the calculation. Default is 1s.
        
        timeColumn 
        - Column to use to compute the elapsed time. Default is _time.
        
        columnName 
        - Column to store elapsed times in. Default is elapsed.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "elapsed"
    package=None

    def __init__(self, unit=None, timeColumn=None, columnName=None, tables=None, ):
            super().__init__(unit=unit, timeColumn=timeColumn, columnName=columnName, tables=tables, )