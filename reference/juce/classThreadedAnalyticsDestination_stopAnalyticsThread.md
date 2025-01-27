#### stopAnalyticsThread()


 void ThreadedAnalyticsDestination::stopAnalyticsThread ( int timeoutMilliseconds ) protected 
 

Triggers the shutdown of the analytics thread.You must call this method in the destructor of your subclass (or before then) to give the analytics thread time to shut down.This method invokes stopLoggingEvents and you should ensure that both the analytics thread and a call to saveUnloggedEvents are able to finish before the supplied timeout. This timeout is important because on platforms like iOS an app is killed if it takes too long to shut down.Parameters

 timeoutMilliseconds the number of milliseconds before the analytics thread is forcibly terminated