#### getText()


 virtual String AudioProcessorParameter::getText ( float normalisedValue, int ) const virtual 
 

Returns a textual version of the supplied normalised parameter value.The default implementation just returns the floating point value as a string, but this could do anything you need for a custom type of value.Reimplemented in AudioPluginInstance::Parameter.