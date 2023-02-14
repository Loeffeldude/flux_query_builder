from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """sql.from() retrieves data from a SQL data source.(Required)
Driver to use to connect to the SQL database.Supported drivers:(Required)
Data source name (DNS) or connection string used to connect
to the SQL database.(Required)
Query to run against the SQL database.

    Params:
        
        driverName 
        - (Required)
Driver to use to connect to the SQL database.Supported drivers:
        
        dataSourceName 
        - (Required)
Data source name (DNS) or connection string used to connect
to the SQL database.
        
        query 
        - (Required)
Query to run against the SQL database.
        
    """
    name = "from"
    package="sql"

    def __init__(self, driverName, dataSourceName, query, ):
            super().__init__(driverName=driverName, dataSourceName=dataSourceName, query=query, )