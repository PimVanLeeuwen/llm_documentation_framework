#### AudioProcessorParameterWithID() [2/2]


 AudioProcessorParameterWithID::AudioProcessorParameterWithID ( const ParameterID & parameterID, 
 
 const String & parameterName, 
 const String & parameterLabel, 
 Category parameterCategory = AudioProcessorParameter::genericParameter ) 

The creation of this object requires providing a name and ID which will be constant for its lifetime.Parameters

 parameterID Used to uniquely identify the parameter 
 
 parameterName The userfacing name of the parameter 
 parameterLabel An optional label for the parameter's value 
 parameterCategory The semantics of this parameter