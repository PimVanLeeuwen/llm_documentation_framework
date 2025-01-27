A class that automatically sends analytics events to the Analytics singleton when a button is clicked.See alsoAnalytics, AnalyticsDestination::AnalyticsEvent 

Constructor & Destructor Documentation


◆ ButtonTracker()


 ButtonTracker::ButtonTracker ( Button & buttonToTrack, 
 
 const String & triggeredEventName, 
 const StringPairArray & triggeredEventParameters = {}, 
 int triggeredEventType = 0 ) 

Creating one of these automatically sends analytics events to the Analytics singleton when the corresponding button is clicked.The name and parameters of the analytics event will be populated from the variables supplied here. If clicking changes the button's state then the parameters will have a {"ButtonState", "On"/"Off"} entry added.Parameters

 buttonToTrack the button to track 
 
 triggeredEventName the name of the generated event 
 triggeredEventParameters the parameters to add to the generated event 
 triggeredEventType (optional) an integer to indicate the event type, which will be set to 0 if not supplied. 



See alsoAnalytics, AnalyticsDestination::AnalyticsEvent 


◆ ~ButtonTracker()


 ButtonTracker::~ButtonTracker ( ) override 
 

Destructor.