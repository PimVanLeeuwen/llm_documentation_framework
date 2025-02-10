#### getDestinations()


 OwnedArray< AnalyticsDestination > & Analytics::getDestinations ( ) 
 

Returns the array of AnalyticsDestinations managed by this class.If you have added any subclasses of ThreadedAnalyticsDestination to this class then you can remove them from this list to force them to flush any pending events.