from flux_query_builder.functions.base import FluxQueryFunction

class APQ(FluxQueryFunction):
    """oee.APQ() computes availability, performance, quality (APQ) and overall equipment
effectiveness (OEE) in producing parts.Provide the required input schema to ensure this function successfully calculates APQ and OEE.Input tables must include the following columns:For each input table, oee.APQ outputs a table with a single row that includes the following columns:(Required)
State value that represents a running state.(Required)
Total time that equipment is expected to produce parts.(Required)
Ideal minimum time to produce one part.Input data. Default is piped-forward data (<-).

    Params:
        
        runningState 
        - (Required)
State value that represents a running state.
        
        plannedTime 
        - (Required)
Total time that equipment is expected to produce parts.
        
        idealCycleTime 
        - (Required)
Ideal minimum time to produce one part.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "APQ"
    package="oee"

    def __init__(self, runningState, plannedTime, idealCycleTime, tables=None, ):
            super().__init__(runningState=runningState, plannedTime=plannedTime, idealCycleTime=idealCycleTime, tables=tables, )