#### getControlParameterIndex()


 virtual int AudioProcessorEditor::getControlParameterIndex ( Component & ) virtual 
 

Called by certain plugin wrappers to find out whether a component is used to control a parameter.If the given component represents a particular plugin parameter, then this method should return the index of that parameter. If not, it should return 1. If not overridden, this will return 1 for all components.This function will be called by the host in AAX and VST3 plugins in order to map screen locations to parameters. For example, in Steinberg hosts, this enables the "AI Knob" functionality, which enables hardware to control the parameter currently under the mouse.