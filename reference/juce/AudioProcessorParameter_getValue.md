#### getValue()


 virtual float AudioProcessorParameter::getValue ( ) const pure virtual 
 

Called by the host to find out the value of this parameter.Hosts will expect the value returned to be between 0 and 1.0.This could be called quite frequently, so try to make your code efficient. It's also likely to be called by nonUI threads, so the code in here should be threadaware.