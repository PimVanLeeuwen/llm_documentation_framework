An object of this class maintains a connection between a Slider and a parameter in an AudioProcessorValueTreeState.During the lifetime of this SliderAttachment object, it keeps the two things in sync, making it easy to connect a slider to a parameter. When this object is deleted, the connection is broken. Make sure that your AudioProcessorValueTreeState and Slider aren't deleted before this object!

Constructor & Destructor Documentation


◆ SliderAttachment()


 AudioProcessorValueTreeState::SliderAttachment::SliderAttachment ( AudioProcessorValueTreeState & stateToUse, 
 
 const String & parameterID, 
 Slider & slider ) 