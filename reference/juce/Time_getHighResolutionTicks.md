#### getHighResolutionTicks()


 static int64 Time::getHighResolutionTicks ( ) staticnoexcept 
 

Returns the current highresolution counter's tickcount.This is a similar idea to getMillisecondCounter(), but with a higher resolution.See alsogetHighResolutionTicksPerSecond, highResolutionTicksToSeconds, secondsToHighResolutionTicks Referenced by ScopedTimeMeasurement::~ScopedTimeMeasurement().