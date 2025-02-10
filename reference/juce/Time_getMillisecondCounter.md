#### getMillisecondCounter()


 static uint32 Time::getMillisecondCounter ( ) staticnoexcept 
 

Returns the number of millisecs since a fixed event (usually system startup).This returns a monotonically increasing value which is unaffected by changes to the system clock. It should be accurate to within a few millisecs, depending on platform, hardware, etc.Being a 32bit return value, it will of course wrap back to 0 after 2^32 seconds of uptime, so be careful to take that into account. If you need a 64bit time, you can use currentTimeMillis() instead.See alsogetApproximateMillisecondCounter