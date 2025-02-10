#### getCurrentTime()


 static Time JUCE\_CALLTYPE Time::getCurrentTime ( ) staticnoexcept 
 

Returns a Time object that is set to the current system time.This may not be monotonic, as the system time can change at any moment. You should therefore not use this method for measuring time intervals.See alsocurrentTimeMillis