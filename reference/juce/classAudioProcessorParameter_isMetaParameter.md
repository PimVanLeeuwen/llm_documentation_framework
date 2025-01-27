#### isMetaParameter()


 virtual bool AudioProcessorParameter::isMetaParameter ( ) const virtual 
 

Should return true if this parameter is a "meta" parameter.A metaparameter is a parameter that changes other params. It is used by some hosts (e.g. AudioUnit hosts). By default this returns false.Reimplemented in AudioProcessorParameterWithID.