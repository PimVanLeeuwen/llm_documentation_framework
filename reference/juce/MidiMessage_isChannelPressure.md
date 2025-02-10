#### isChannelPressure()


 bool MidiMessage::isChannelPressure ( ) const noexcept 
 

Returns true if the message is a channelpressure change event.This is like aftertouch, but common to the whole channel rather than a specific note. Use getChannelPressureValue() to find out the pressure, and getChannel() to find out the channel.See alsochannelPressureChange