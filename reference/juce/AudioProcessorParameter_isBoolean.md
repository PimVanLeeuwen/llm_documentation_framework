#### isBoolean()


 virtual bool AudioProcessorParameter::isBoolean ( ) const virtual 
 

Returns whether the parameter represents a boolean switch, typically with "On" and "Off" states.This information may or may not be used, depending on the host. If you want the host to display a switch, rather than a two item dropdown menu, override this method to return true. You also need to override isDiscrete() to return `true` and getNumSteps() to return `2`.See alsoisDiscrete getNumSteps Reimplemented in AudioProcessorValueTreeState::Parameter.