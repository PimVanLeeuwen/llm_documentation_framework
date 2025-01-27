#### ensureStorageAllocated()


 void MidiMessageCollector::ensureStorageAllocated ( size\_t bytes ) 
 

Preallocates storage for collected messages.This can be called before audio processing begins to ensure that there is sufficient space for the expected MIDI messages, in order to avoid allocations within the audio callback.