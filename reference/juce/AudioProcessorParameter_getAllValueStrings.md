#### getAllValueStrings()


 virtual StringArray AudioProcessorParameter::getAllValueStrings ( ) const virtual 
 

Returns the set of strings which represent the possible states a parameter can be in.If you are hosting a plugin you can use the result of this function to populate a ComboBox listing the allowed values.If you are implementing a plugin then you do not need to override this.