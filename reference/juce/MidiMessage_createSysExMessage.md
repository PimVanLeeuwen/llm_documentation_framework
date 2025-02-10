#### createSysExMessage() [2/2]


 static MidiMessage MidiMessage::createSysExMessage ( Span< const std::byte > data ) static 
 

Creates a systemexclusive message.The data passed in is wrapped with header and tail bytes of 0xf0 and 0xf7.