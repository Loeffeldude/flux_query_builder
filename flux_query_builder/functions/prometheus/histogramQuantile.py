from flux_query_builder.functions.base import FluxQueryFunction

class HistogramQuantile(FluxQueryFunction):
    """prometheus.histogramQuantile() calculates a quantile on a set of Prometheus histogram values.This function supports Prometheus metric parsing formats
used by prometheus.scrape(), the Telegraf promtheus input plugin, and
InfluxDB scrapers available in InfluxDB OSS.(Required)
Quantile to compute. Must be a float value between 0.0 and 1.0.Prometheus metric parsing format
used to parse queried Prometheus data.
Available versions are 1 and 2.
Default is 2.Input data. Default is piped-forward data (<-).

    Params:
        
        quantile 
        - (Required)
Quantile to compute. Must be a float value between 0.0 and 1.0.
        
        metricVersion 
        - Prometheus metric parsing format
used to parse queried Prometheus data.
Available versions are 1 and 2.
Default is 2.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "histogramQuantile"
    package="prometheus"

    def __init__(self, quantile, metricVersion=None, tables=None, ):
            super().__init__(quantile=quantile, metricVersion=metricVersion, tables=tables, )