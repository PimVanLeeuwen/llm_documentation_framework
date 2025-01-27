#### timestamp


 uint32 AnalyticsDestination::AnalyticsEvent::timestamp 
 

The timestamp of the event.Timestamps are automatically applied by an Analytics object and are derived from Time::getMillisecondCounter(). As such these timestamps do not represent absolute times, but relative timings of events for each user in each session will be accurate.