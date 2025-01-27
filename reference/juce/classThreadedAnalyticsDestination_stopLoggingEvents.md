#### stopLoggingEvents()


 virtual void ThreadedAnalyticsDestination::stopLoggingEvents ( ) pure virtual 
 

You must always call stopAnalyticsThread in the destructor of your subclass (or before then) to give the analytics thread time to shut down.Calling stopAnalyticsThread triggers a call to this method. At this point you are guaranteed that logBatchedEvents has been called for the last time and you should make sure that the current call to logBatchedEvents finishes as quickly as possible. This method and a subsequent call to saveUnloggedEvents must both complete before the timeout supplied to stopAnalyticsThread.In a normal use case stopLoggingEvents will be called on the message thread from the destructor of your ThreadedAnalyticsDestination subclass, and must stop the logBatchedEvents method which is running on the analytics thread.See alsostopAnalyticsThread