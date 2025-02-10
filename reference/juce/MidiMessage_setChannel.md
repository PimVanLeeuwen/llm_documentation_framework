#### setChannel()


 void MidiMessage::setChannel ( int newChannelNumber ) noexcept 
 

Changes the message's midi channel.This won't do anything for nonchannel messages like sysexes.Parameters

 newChannelNumber the channel number to change it to, in the range 1 to 16