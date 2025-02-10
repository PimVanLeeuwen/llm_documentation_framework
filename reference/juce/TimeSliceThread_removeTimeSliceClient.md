#### removeTimeSliceClient()


 void TimeSliceThread::removeTimeSliceClient ( TimeSliceClient \* clientToRemove ) 
 

Removes a client from the list.This method will make sure that all callbacks to the client have completely finished before the method returns.