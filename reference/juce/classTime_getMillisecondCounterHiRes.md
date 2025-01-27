#### getMillisecondCounterHiRes()


 static double Time::getMillisecondCounterHiRes ( ) staticnoexcept 
 

Returns the number of millisecs since a fixed event (usually system startup).This has the same function as getMillisecondCounter(), but returns a more accurate value, using a higherresolution timer if one is available.See alsogetMillisecondCounter