#### generate() [2/2]


 static MidiBuffer MidiRPNGenerator::generate ( int channel, int parameterNumber, int value, bool isNRPN = false, bool use14BitValue = true ) static 
 

Generates a MIDI sequence representing an RPN or NRPN message with the given parameters.Parameters

 channel The MIDI channel of the RPN/NRPN message. 
 
 parameterNumber The parameter number, in the range 0 to 16383. 
 value The parameter value, in the range 0 to 16383, or in the range 0 to 127 if sendAs14BitValue is false. 
 isNRPN Whether you need a MIDI RPN or NRPN sequence (RPN is default). 
 use14BitValue If true (default), the value will have 14bit precision (two MIDI bytes). If false, instead the value will have 7bit precision (a single MIDI byte).