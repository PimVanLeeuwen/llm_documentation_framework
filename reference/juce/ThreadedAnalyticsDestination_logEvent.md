#### logEvent()


 void ThreadedAnalyticsDestination::logEvent ( const AnalyticsEvent & event ) finaloverridevirtual 
 

Adds an event to the queue, which will ultimately be submitted to logBatchedEvents.This method is thread safe.Parameters

 event the analytics event to add to the queue 
 


Implements AnalyticsDestination.