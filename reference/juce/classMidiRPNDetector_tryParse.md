#### tryParse()


 std::optional< MidiRPNMessage > MidiRPNDetector::tryParse ( int midiChannel, 
 
 int controllerNumber, 
 int controllerValue ) 

Takes the next in a stream of incoming MIDI CC messages and returns a MidiRPNMessage if the current message produces a wellformed RPN or NRPN.Note that senders are expected to send the MSB before the LSB, but senders are not required to send a LSB at all. Therefore, tryParse() will return a nonnull optional on all MSB messages (provided a parameter number has been set), and will also return a nonnull optional for each LSB that follows the initial MSB.This behaviour allows senders to transmit a single MSB followed by multiple LSB messages to facilitate finetuning of parameters.The result of parsing a MSB will always be a 7bit value. The result of parsing a LSB that follows an MSB will always be a 14bit value.