#### isMidiMachineControlMessage()


 bool MidiMessage::isMidiMachineControlMessage ( ) const noexcept 
 

Checks whether this is an MMC message.If it is, you can use the getMidiMachineControlCommand() to find out its type.