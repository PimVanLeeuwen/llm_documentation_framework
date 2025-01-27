#### handleIncomingMidiMessage()


 virtual void MidiInputCallback::handleIncomingMidiMessage ( MidiInput \* source, const MidiMessage & message ) pure virtual 
 

Receives an incoming message.A MidiInput object will call this method when a midi event arrives. It'll be called on a highpriority system thread, so avoid doing anything timeconsuming in here, and avoid making any UI calls. You might find the MidiBuffer class helpful for queueing incoming messages for use later.Parameters

 source the MidiInput object that generated the message 
 
 message the incoming message. The message's timestamp is set to a value equivalent to (Time::getMillisecondCounter() / 1000.0) to specify the time when the message arrived 


Implemented in AudioProcessorPlayer, and MidiMessageCollector.