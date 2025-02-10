#### getHoursInAmPmFormat()


 int Time::getHoursInAmPmFormat ( ) const noexcept 
 

Returns the hours in 12hour clock format (in this machine's local timezone).This will return a value 1 to 12 use isAfternoon() to find out whether this is in the afternoon or morning.See alsogetHours, isAfternoon