#### getApproximateMillisecondCounter()


 static uint32 Time::getApproximateMillisecondCounter ( ) staticnoexcept 
 

Lessaccurate but faster version of getMillisecondCounter().This will return the last value that getMillisecondCounter() returned, so doesn't need to make a system call, but is less accurate it shouldn't be more than 100ms away from the correct time, though, so is still accurate enough for a lot of purposes.See alsogetMillisecondCounter