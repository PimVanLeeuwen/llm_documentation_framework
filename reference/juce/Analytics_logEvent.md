#### logEvent()


 void Analytics::logEvent ( const String & eventName, 
 
 const StringPairArray & parameters, 
 int eventType = 0 ) 

Sends an AnalyticsEvent to all AnalyticsDestinations.The AnalyticsEvent will be timestamped, and will have the userId and userProperties populated by values previously set by calls to setUserId and setUserProperties. The name, parameters and type will be populated by the arguments supplied to this function.Parameters

 eventName the event name 
 
 parameters the event parameters 
 eventType (optional) an integer to indicate the event type, which will be set to 0 if not supplied.