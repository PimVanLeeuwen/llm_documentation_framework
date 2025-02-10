#### setBatchPeriod()


 void ThreadedAnalyticsDestination::setBatchPeriod ( int newSubmissionPeriodMilliseconds ) 
 

Call this to set the period between logBatchedEvents invocations.This method is thread safe and can be used to implements things like exponential backoff in logBatchedEvents calls.Parameters

 newSubmissionPeriodMilliseconds the new submission period to use in milliseconds