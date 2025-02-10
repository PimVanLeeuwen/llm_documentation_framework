#### updateHostDisplay()


 void AudioProcessor::updateHostDisplay ( const ChangeDetails & details = ChangeDetails::getDefaultFlags() ) 
 

The processor can call this when something (apart from a parameter value) has changed.It sends a hint to the host that something like the program, number of parameters, etc, has changed, and that it should update itself.