#### useTimeSlice()


 virtual int TimeSliceClient::useTimeSlice ( ) pure virtual 
 

Called back by a TimeSliceThread.When you register this class with it, a TimeSliceThread will repeatedly call this method.The implementation of this method should use its timeslice to do something that's quick never block for longer than absolutely necessary.ReturnsYour method should return the number of milliseconds which it would like to wait before being called again. Returning 0 will make the thread call again as soon as possible (after possibly servicing other busy clients). If you return a value below zero, your client will be removed from the list of clients, and won't be called again. The value you specify isn't a guarantee, and is only used as a hint by the thread the actual time before the next callback may be more or less than specified. You can force the TimeSliceThread to wake up and poll again immediately by calling its notify() method.