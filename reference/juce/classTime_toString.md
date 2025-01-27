#### toString()


 String Time::toString ( bool includeDate, 
 
 bool includeTime, 
 bool includeSeconds = true, 
 bool use24HourClock = false ) const 

Returns a string version of this date and time, using this machine's local timezone.For a more powerful way of formatting the date and time, see the formatted() method.Parameters

 includeDate whether to include the date in the string 
 
 includeTime whether to include the time in the string 
 includeSeconds if the time is being included, this provides an option not to include the seconds in it 
 use24HourClock if the time is being included, sets whether to use am/pm or 24 hour notation. 



See alsoformatted