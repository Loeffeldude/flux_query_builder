from flux_query_builder.functions.base import FluxQueryFunction

class Alert(FluxQueryFunction):
    """tickscript.alert() identifies events of varying severity levels
and writes them to the statuses measurement in the InfluxDB _monitoring
system bucket.This function is comparable to
TICKscript alert().(Required)
InfluxDB check data.
See tickscript.defineCheck().Function that returns the InfluxDB check ID provided by the check record.
Default is (r) => "${r._check_id}".Function to return the InfluxDB check details using data from input rows.
Default is (r) => "".Function to return the InfluxDB check message using data from input rows.
Default is (r) => "Threshold Check: ${r._check_name} is: ${r._level}".Predicate function to determine crit status. Default is (r) => false.Predicate function to determine warn status. Default is (r) => false.Predicate function to determine info status. Default is (r) => false.Predicate function to determine ok status. Default is (r) => true.Check topic. Default is "".Input data. Default is piped-forward data (<-).

    Params:
        
        check 
        - (Required)
InfluxDB check data.
See tickscript.defineCheck().
        
        id 
        - Function that returns the InfluxDB check ID provided by the check record.
Default is (r) => "${r._check_id}".
        
        details 
        - Function to return the InfluxDB check details using data from input rows.
Default is (r) => "".
        
        message 
        - Function to return the InfluxDB check message using data from input rows.
Default is (r) => "Threshold Check: ${r._check_name} is: ${r._level}".
        
        crit 
        - Predicate function to determine crit status. Default is (r) => false.
        
        warn 
        - Predicate function to determine warn status. Default is (r) => false.
        
        info 
        - Predicate function to determine info status. Default is (r) => false.
        
        ok 
        - Predicate function to determine ok status. Default is (r) => true.
        
        topic 
        - Check topic. Default is "".
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "alert"
    package="tickscript"

    def __init__(self, check, id=None, details=None, message=None, crit=None, warn=None, info=None, ok=None, topic=None, tables=None, ):
            super().__init__(check=check, id=id, details=details, message=message, crit=crit, warn=warn, info=info, ok=ok, topic=topic, tables=tables, )