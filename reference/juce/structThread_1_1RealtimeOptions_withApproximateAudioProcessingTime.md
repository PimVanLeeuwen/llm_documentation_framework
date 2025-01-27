#### withApproximateAudioProcessingTime()


 RealtimeOptions Thread::RealtimeOptions::withApproximateAudioProcessingTime ( int samplesPerFrame, double sampleRate ) const nodiscard 
 

Specify the maximum amount of processing time required each time the thread wakes up.This is identical to 'withMaximumProcessingTimeMs' except it calculates the processing time from a sample rate and block size. This is useful if you want to run this thread in parallel to an audio device thread.Only used by macOS/iOS.See alsowithMaximumProcessingTimeMs, AudioWorkgroup, ScopedWorkgroupToken References jassert.