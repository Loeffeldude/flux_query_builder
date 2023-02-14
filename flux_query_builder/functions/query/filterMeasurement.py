from flux_query_builder.functions.base import FluxQueryFunction

class FilterMeasurement(FluxQueryFunction):
    """query.filterMeasurement() filters input data by measurement.(Required)
InfluxDB measurement name to filter by.Input data. Default is piped-forward data (<-).

    Params:
        
        measurement 
        - (Required)
InfluxDB measurement name to filter by.
        
        table 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "filterMeasurement"
    package="query"

    def __init__(self, measurement, table=None, ):
            super().__init__(measurement=measurement, table=table, )