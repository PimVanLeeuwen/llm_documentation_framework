#### withPeriodMs()


 RealtimeOptions Thread::RealtimeOptions::withPeriodMs ( double newPeriodMs ) const nodiscard 
 

Specify the approximate amount of time between each thread wake up.Alternatively call withPeriodHz().Only used by macOS/iOS.See alsogetPeriodMs, withPeriodHz, withProcessingTimeMs, withMaximumProcessingTimeMs, References jassert, and withMember().