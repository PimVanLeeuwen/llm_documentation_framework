#### addBlob()


 void OSCMessage::addBlob ( MemoryBlock blob ) 
 

Creates a new OSCArgument of type blob with binary data content copied from the given MemoryBlock.Note: If the argument passed is an lvalue, this may copy the binary data.