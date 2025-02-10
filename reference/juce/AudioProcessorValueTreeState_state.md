#### state


 ValueTree AudioProcessorValueTreeState::state 
 

The state of the whole processor.This must be initialised after all calls to createAndAddParameter(). You can replace this with your own ValueTree object, and can add properties and children to the tree. This class will automatically add children for each of the parameter objects that are created by createAndAddParameter().