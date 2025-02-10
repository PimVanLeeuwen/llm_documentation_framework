#### moveToFrontOfQueue()


 void TimeSliceThread::moveToFrontOfQueue ( TimeSliceClient \* clientToMove ) 
 

If the given client is waiting in the queue, it will be moved to the front and given a timeslice as soon as possible.If the specified client has not been added, nothing will happen.