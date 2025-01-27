#### addArgument()


 void OSCMessage::addArgument ( OSCArgument argument ) 
 

Adds the OSCArgument argument to the OSCMessage object.Note: This method will result in a copy of the OSCArgument object if it is passed as an lvalue. If the OSCArgument is of type blob, this will also copy the underlying binary data. In general, you should use addInt32, addFloat32, etc. instead.