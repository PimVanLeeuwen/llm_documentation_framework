#### addEvent() [2/2]


 bool MidiBuffer::addEvent ( const void \* rawMidiData, 
 
 int maxBytesOfMidiData, 
 int sampleNumber ) 

Adds an event to the buffer from raw midi data.The sample number will be used to determine the position of the event in the buffer, which is always kept sorted.If an event is added whose sample position is the same as one or more events already in the buffer, the new event will be placed after the existing ones.The event data will be inspected to calculate the number of bytes in length that the midi event really takes up, so maxBytesOfMidiData may be longer than the data that actually gets stored. E.g. if you pass in a noteon and a length of 4 bytes, it'll actually only store 3 bytes. If the midi data is invalid, it might not add an event at all.To retrieve events, use a MidiBufferIterator object.Returns true on success, or false on failure.