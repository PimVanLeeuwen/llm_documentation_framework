#### getBlob()


 const MemoryBlock & OSCArgument::getBlob ( ) const noexcept 
 

Returns the binary data contained in the blob and owned by the OSCArgument, as a reference to a JUCE MemoryBlock object.If the type of the OSCArgument is not blob, the behaviour is undefined.