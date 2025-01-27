#### getMaximumBatchSize()


 virtual int ThreadedAnalyticsDestination::getMaximumBatchSize ( ) pure virtual 
 

Override this method to provide the maximum batch size you can handle in your subclass.Calls to logBatchedEvents will contain no more than this number of events.