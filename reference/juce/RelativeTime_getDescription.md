#### getDescription()


 String RelativeTime::getDescription ( const String & returnValueForZeroTime = "0" ) const 
 

Returns a readable textual description of the time.The exact format of the string returned will depend on the magnitude of the time e.g."1 min 4 secs", "1 hr 45 mins", "2 weeks 5 days", "140 ms"so that only the two most significant units are printed.The returnValueForZeroTime value is the result that is returned if the length is zero. Depending on your application you might want to use this to return something more relevant like "empty" or "0 secs", etc.See alsoinMilliseconds, inSeconds, inMinutes, inHours, inDays, inWeeks