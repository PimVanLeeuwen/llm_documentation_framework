#### getMilliseconds()


 int Time::getMilliseconds ( ) const noexcept 
 

Returns the number of milliseconds, 0 to 999.Unlike toMilliseconds(), this just returns the position within the current second rather than the total number since the epoch.See alsotoMilliseconds