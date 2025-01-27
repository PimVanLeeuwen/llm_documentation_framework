#### withPeriodHz()


 RealtimeOptions Thread::RealtimeOptions::withPeriodHz ( double newPeriodHz ) const nodiscard 
 

Specify the approximate frequency at which the thread will be woken up.Alternatively call withPeriodMs().Only used by macOS/iOS.See alsogetPeriodHz, withPeriodMs, withProcessingTimeMs, withMaximumProcessingTimeMs, References jassert.