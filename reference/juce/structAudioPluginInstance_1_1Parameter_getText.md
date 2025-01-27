#### getText()


 String AudioPluginInstance::Parameter::getText ( float normalisedValue, int ) const overridevirtual 
 

Returns a textual version of the supplied normalised parameter value.The default implementation just returns the floating point value as a string, but this could do anything you need for a custom type of value.Reimplemented from AudioProcessorParameter.