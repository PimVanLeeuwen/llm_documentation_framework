#### getApproximateDescription()


 String RelativeTime::getApproximateDescription ( ) const 
 

This returns a string that roughly describes how long ago this time was, which can be handy for showing ages of files, etc.This will only attempt to be accurate to within the nearest order of magnitude so returns strings such as "5 years", "2 weeks", "< 1 minute", "< 1 sec" etc.