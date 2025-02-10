#### isMidiMachineControlGoto()


 bool MidiMessage::isMidiMachineControlGoto ( int & hours, int & minutes, int & seconds, int & frames ) const noexcept 
 

Checks whether this is an MMC "goto" message.If it is, the parameters passedin are set to the time that the message contains.See alsomidiMachineControlGoto