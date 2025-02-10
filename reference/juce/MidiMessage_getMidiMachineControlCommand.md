#### getMidiMachineControlCommand()


 MidiMachineControlCommand MidiMessage::getMidiMachineControlCommand ( ) const noexcept 
 

For an MMC message, this returns its type.Make sure it's actually an MMC message with isMidiMachineControlMessage() before calling this method.