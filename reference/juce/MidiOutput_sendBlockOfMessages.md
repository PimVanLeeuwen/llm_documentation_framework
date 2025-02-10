#### sendBlockOfMessages()


 void MidiOutput::sendBlockOfMessages ( const MidiBuffer & buffer, 
 
 double millisecondCounterToStartAt, 
 double samplesPerSecondForBuffer ) 

This lets you supply a block of messages that will be sent out at some point in the future.The MidiOutput class has an internal thread that can send out timestamped messages this appends a set of messages to its internal buffer, ready for sending.This will only work if you've already started the thread with startBackgroundThread().A time is specified, at which the block of messages should be sent. This time uses the same time base as Time::getMillisecondCounter(), and must be in the future.The samplesPerSecondForBuffer parameter indicates the number of samples per second used by the MidiBuffer. Each event in a MidiBuffer has a sample position, and the samplesPerSecondForBuffer value is needed to convert this sample position to a real time.