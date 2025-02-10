#### addTimeSliceClient()


 void TimeSliceThread::addTimeSliceClient ( TimeSliceClient \* clientToAdd, 
 
 int millisecondsBeforeStarting = 0 ) 

Adds a client to the list.The client's callbacks will start after the number of milliseconds specified by millisecondsBeforeStarting (and this may happen before this method has returned).