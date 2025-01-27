#### removeNextBlockOfMessages()


 void MidiMessageCollector::removeNextBlockOfMessages ( MidiBuffer & destBuffer, 
 
 int numSamples ) 

Removes all the pending messages from the queue as a buffer.This will also correct the messages' timestamps to make sure they're in the range 0 to numSamples 1.This call should be made regularly by something like an audio processing callback, because the time that it happens is used in calculating the midi event positions.This method is fully threadsafe when overlapping calls are made with addMessageToQueue().Precondition: numSamples must be greater than 0.