An object of this class maintains a connection between a Button and a parameter in an AudioProcessorValueTreeState.During the lifetime of this ButtonAttachment object, it keeps the two things in sync, making it easy to connect a button to a parameter. When this object is deleted, the connection is broken. Make sure that your AudioProcessorValueTreeState and Button aren't deleted before this object!

Constructor & Destructor Documentation


◆ ButtonAttachment()


 AudioProcessorValueTreeState::ButtonAttachment::ButtonAttachment ( AudioProcessorValueTreeState & stateToUse, 
 
 const String & parameterID, 
 Button & button ) 