from flux_query_builder.functions.base import FluxQueryFunction

class Check(FluxQueryFunction):
    """monitor.check() checks input data and assigns a level (ok, info, warn, or crit)
to each row based on predicate functions.monitor.check() stores statuses in the _level column and writes results
to the statuses measurement in the _monitoring bucket.Predicate function that determines crit status. Default is (r) => false.Predicate function that determines warn status. Default is (r) => false.Predicate function that determines info status. Default is (r) => false.Predicate function that determines ok status. Default is (r) => true.(Required)
Predicate function that constructs a message to append to each row.The message is stored in the _message column.(Required)
Check data to append to output used to identify this check.This data specifies which notification rule and notification endpoint to
associate with the sent notification.
The data record must contain the following properties:Input data. Default is piped-forward data (<-).

    Params:
        
        messageFn 
        - (Required)
Predicate function that constructs a message to append to each row.The message is stored in the _message column.
        
        data 
        - (Required)
Check data to append to output used to identify this check.This data specifies which notification rule and notification endpoint to
associate with the sent notification.
The data record must contain the following properties:
        
        crit 
        - Predicate function that determines crit status. Default is (r) => false.
        
        warn 
        - Predicate function that determines warn status. Default is (r) => false.
        
        info 
        - Predicate function that determines info status. Default is (r) => false.
        
        ok 
        - Predicate function that determines ok status. Default is (r) => true.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "check"
    package="monitor"

    def __init__(self, messageFn, data, crit=None, warn=None, info=None, ok=None, tables=None, ):
            super().__init__(messageFn=messageFn, data=data, crit=crit, warn=warn, info=info, ok=ok, tables=tables, )