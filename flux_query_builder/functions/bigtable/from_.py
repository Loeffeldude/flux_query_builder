from flux_query_builder.functions.base import FluxQueryFunction

class From(FluxQueryFunction):
    """bigtable.from() retrieves data from a Google Cloud Bigtable data source.(Required)
Google Cloud IAM token to use to access the Cloud Bigtable database.For more information, see the following:(Required)
Cloud Bigtable project ID.(Required)
Cloud Bigtable instance ID.(Required)
Cloud Bigtable table name.

    Params:
        
        token 
        - (Required)
Google Cloud IAM token to use to access the Cloud Bigtable database.For more information, see the following:
        
        project 
        - (Required)
Cloud Bigtable project ID.
        
        instance 
        - (Required)
Cloud Bigtable instance ID.
        
        table 
        - (Required)
Cloud Bigtable table name.
        
    """
    name = "from"
    package="bigtable"

    def __init__(self, token, project, instance, table, ):
            super().__init__(token=token, project=project, instance=instance, table=table, )