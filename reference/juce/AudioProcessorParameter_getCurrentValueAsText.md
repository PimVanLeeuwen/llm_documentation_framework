#### getCurrentValueAsText()


 virtual String AudioProcessorParameter::getCurrentValueAsText ( ) const virtual 
 

Returns the current value of the parameter as a String.This function can be called when you are hosting plugins to get a more specialised textual representation of the current value from the plugin, for example "On" rather than "1.0".If you are implementing a plugin then you should ignore this function and instead override getText.