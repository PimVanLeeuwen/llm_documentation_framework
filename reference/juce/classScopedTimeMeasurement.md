Simple RAII class for measuring the time spent in a scope.Example:{ double timeSec;{ ScopedTimeMeasurement m (timeSec); doSomething(); }Logger::writeToLog ("doSomething() took " + String (timeSec) + "seconds"); }Parameters

 resultInSeconds The result of the measurement will be stored in this variable. 
 



Constructor & Destructor Documentation


◆ ScopedTimeMeasurement()


 ScopedTimeMeasurement::ScopedTimeMeasurement ( double & resultInSeconds ) noexcept 
 



◆ ~ScopedTimeMeasurement()


 ScopedTimeMeasurement::~ScopedTimeMeasurement ( ) 
 

References Time::getHighResolutionTicks(), and Time::getHighResolutionTicksPerSecond().