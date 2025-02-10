#### isDiscrete()


 bool AudioProcessorValueTreeState::Parameter::isDiscrete ( ) const overridevirtual 
 

Returns whether the parameter uses discrete values, based on the result of getNumSteps, or allows the host to select values continuously.This information may or may not be used, depending on the host. If you want the host to display stepped automation values, rather than a continuous interpolation between successive values, override this method to return true.See alsogetNumSteps Reimplemented from AudioProcessorParameter.