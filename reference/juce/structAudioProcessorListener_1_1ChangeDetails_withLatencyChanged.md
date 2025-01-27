#### withLatencyChanged()


 ChangeDetails AudioProcessorListener::ChangeDetails::withLatencyChanged ( bool b ) const nodiscardnoexcept 
 

Indicates that the AudioProcessor's latency has changed.Most of the time, you won't need to use this function directly. AudioProcessor::setLatencySamples() will automatically call AudioProcessor::updateHostDisplay(), indicating that the latency has changed.See alsolatencyChanged Referenced by getDefaultFlags().