#### getNumSteps()


 int RangedAudioParameter::getNumSteps ( ) const overridevirtual 
 

Returns the number of steps for this parameter based on the normalisable range's interval.If you are using lambda functions to define the normalisable range's snapping behaviour then you should override this function so that it returns the number of snapping points.Reimplemented from AudioProcessorParameter.