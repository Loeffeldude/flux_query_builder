from flux_query_builder.functions.base import FluxQueryFunction

class NaiveBayes(FluxQueryFunction):
    """naiveBayesClassifier.naiveBayes() performs a naive Bayes classification.(Required)
Measurement to use as training data.(Required)
Field to use as training data.(Required)
Class to classify against.Input data. Default is piped-forward data (<-).

    Params:
        
        myMeasurement 
        - (Required)
Measurement to use as training data.
        
        myField 
        - (Required)
Field to use as training data.
        
        myClass 
        - (Required)
Class to classify against.
        
        tables 
        - Input data. Default is piped-forward data (<-).
        
    """
    name = "naiveBayes"
    package="naiveBayesClassifier"

    def __init__(self, myMeasurement, myField, myClass, tables=None, ):
            super().__init__(myMeasurement=myMeasurement, myField=myField, myClass=myClass, tables=tables, )