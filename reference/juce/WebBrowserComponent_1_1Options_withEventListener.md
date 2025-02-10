#### withEventListener()


 Options WebBrowserComponent::Options::withEventListener ( const Identifier & eventId, NativeEventListener listener ) const nodiscard 
 

Registers a NativeEventListener that receives events sent to the specified eventId.To send a message to this listener from the frontend, call for examplewindow.\_\_JUCE\_\_.backend.emitEvent(eventId, { x: 2, y: 6 }); 
xfloat xDefinition juce\_UnityPluginInterface.h:200
yfloat float yDefinition juce\_UnityPluginInterface.h:200
AccessibilityRole::window@ window
Referenced by WebControlParameterIndexReceiver::buildOptions().