from flux_query_builder.functions.base import FluxQueryFunction

class Mad(FluxQueryFunction):
    """anomalydetection.mad() uses the median absolute deviation (MAD) algorithm to detect anomalies in a data set.Input data requires _time and _value columns.
Output data is grouped by _time and includes the following columns of interest:Deviation threshold for anomalies.Input data. Default is piped-forward data (<-).

    Params:
        
        threshold 
        - Deviation threshold for anomalies.
        
        table 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "mad"
    package="anomalydetection"

    def __init__(self, threshold=None, table=None, ):
            super().__init__(threshold=threshold, table=table, )