from flux_query_builder.functions.base import FluxQueryFunction

class Scrape(FluxQueryFunction):
    """prometheus.scrape() scrapes Prometheus metrics from an HTTP-accessible endpoint and returns
them as a stream of tables.(Required)
URL to scrape Prometheus metrics from.

    Params:
        
        url 
        - (Required)
URL to scrape Prometheus metrics from.
        
    """
    name = "scrape"
    package="prometheus"

    def __init__(self, url, ):
            super().__init__(url=url, )