#### processBlockBypassed() [2/2]


 virtual void AudioProcessor::processBlockBypassed ( AudioBuffer< double > & buffer, MidiBuffer & midiMessages ) virtual 
 

Renders the next block when the processor is being bypassed.The default implementation of this method will passthrough any incoming audio, but you may override this method e.g. to add latency compensation to the data to match the processor's latency characteristics. This will avoid situations where bypassing will shift the signal forward in time, possibly creating preecho effects and odd timings. Another use for this method would be to crossfade or morph between the wet (not bypassed) and dry (bypassed) signals.