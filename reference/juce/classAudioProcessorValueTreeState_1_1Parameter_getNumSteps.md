#### getNumSteps()


 int AudioProcessorValueTreeState::Parameter::getNumSteps ( ) const overridevirtual 
 

Returns the number of steps that this parameter's range should be quantised into.If you want a continuous range of values, don't override this method, and allow the default implementation to return AudioProcessor::getDefaultNumParameterSteps().If your parameter is boolean, then you may want to make this return 2.The value that is returned may or may not be used, depending on the host. If you want the host to display stepped automation values, rather than a continuous interpolation between successive values, you should override isDiscrete to return true.See alsoisDiscrete Reimplemented from AudioParameterFloat.