from flux_query_builder.functions.base import FluxQueryFunction

class ComputeAPQ(FluxQueryFunction):
    """oee.computeAPQ() computes availability, performance, and quality (APQ)
and overall equipment effectiveness (OEE) using two separate input streams:
production events and part events.For each input table, oee.computeAPQ outputs a table with a single row and
the following columns:(Required)
Production events stream that contains the production
state or start and stop events.Each row must contain the following columns:(Required)
Part events that contains the running totals of parts produced and
parts that do not meet quality standards.Each row must contain the following columns:(Required)
State value that represents a running state.(Required)
Total time that equipment is expected to produce parts.(Required)
Ideal minimum time to produce one part.

    Params:
        
        productionEvents 
        - (Required)
Production events stream that contains the production
state or start and stop events.Each row must contain the following columns:
        
        partEvents 
        - (Required)
Part events that contains the running totals of parts produced and
parts that do not meet quality standards.Each row must contain the following columns:
        
        runningState 
        - (Required)
State value that represents a running state.
        
        plannedTime 
        - (Required)
Total time that equipment is expected to produce parts.
        
        idealCycleTime 
        - (Required)
Ideal minimum time to produce one part.
        
    """
    name = "computeAPQ"
    package="oee"

    def __init__(self, productionEvents, partEvents, runningState, plannedTime, idealCycleTime, ):
            super().__init__(productionEvents=productionEvents, partEvents=partEvents, runningState=runningState, plannedTime=plannedTime, idealCycleTime=idealCycleTime, )