#### processNextMidiBuffer()


 void MidiKeyboardState::processNextMidiBuffer ( MidiBuffer & buffer, 
 
 int startSample, 
 int numSamples, 
 bool injectIndirectEvents ) 

Scans a midi stream for up/down events and adds its own events to it.This will look for any up/down events and use them to update the internal state, synchronously making suitable callbacks to the listeners.If injectIndirectEvents is true, then midi events to produce the recent noteOn() and noteOff() calls will be added into the buffer.Only the section of the buffer whose timestamps are between startSample and (startSample + numSamples) will be affected, and any events added will be placed between these times.If you're going to use this method, you'll need to keep calling it regularly for it to work satisfactorily.To process a single midi event at a time, use the processNextMidiEvent() method instead.