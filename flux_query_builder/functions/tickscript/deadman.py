from flux_query_builder.functions.base import FluxQueryFunction

class Deadman(FluxQueryFunction):
    """tickscript.deadman() detects low data throughput and writes a point with a critical status to
the InfluxDB _monitoring system bucket.For each input table containing a number of rows less than or equal to the specified threshold,
the function assigns a crit value to the _level column.This function is comparable to Kapacitor AlertNode deadman.(Required)
InfluxDB check data. See tickscript.defineCheck().(Required)
Measurement name. Should match the queried measurement.Count threshold. Default is 0.The function assigns a crit status to input tables with a number of rows less than or equal to the threshold.Function that returns the InfluxDB check ID provided by the check record.
Default is (r) => "${r._check_id}".Function that returns the InfluxDB check message using data from input rows.
Default is (r) => "Deadman Check: ${r._check_name} is: " + (if r.dead then "dead" else "alive").Check topic. Default is "".Input data. Default is piped-forward data (<-).

    Params:
        
        check 
        - (Required)
InfluxDB check data. See tickscript.defineCheck().
        
        measurement 
        - (Required)
Measurement name. Should match the queried measurement.
        
        threshold 
        - Count threshold. Default is 0.The function assigns a crit status to input tables with a number of rows less than or equal to the threshold.
        
        id 
        - Function that returns the InfluxDB check ID provided by the check record.
Default is (r) => "${r._check_id}".
        
        message 
        - Function that returns the InfluxDB check message using data from input rows.
Default is (r) => "Deadman Check: ${r._check_name} is: " + (if r.dead then "dead" else "alive").
        
        topic 
        - Check topic. Default is "".
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "deadman"
    package="tickscript"

    def __init__(self, check, measurement, threshold=None, id=None, message=None, topic=None, tables=None, ):
            super().__init__(check=check, measurement=measurement, threshold=threshold, id=id, message=message, topic=topic, tables=tables, )