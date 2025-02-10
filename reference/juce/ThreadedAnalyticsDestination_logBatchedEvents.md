#### logBatchedEvents()


 virtual bool ThreadedAnalyticsDestination::logBatchedEvents ( const Array< AnalyticsEvent > & events ) pure virtual 
 

This method will be called periodically on the analytics thread.If this method returns false then the subsequent call of this function will contain the same events as previous call, plus any new events that have been generated in the period between calls. The order of events will not be changed. This allows you to retry logging events until they are logged successfully.Parameters

 events a list of events to be logged 
 



Returnsif the events were successfully logged