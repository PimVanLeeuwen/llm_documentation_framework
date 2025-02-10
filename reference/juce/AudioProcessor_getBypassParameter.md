#### getBypassParameter()


 virtual AudioProcessorParameter \* AudioProcessor::getBypassParameter ( ) const virtual 
 

Returns the parameter that controls the AudioProcessor's bypass state.If this method returns a nullptr then you can still control the bypass by calling processBlockBypassed instead of processBlock. On the other hand, if this method returns a nonnull value, you should never call processBlockBypassed but use the returned parameter to control the bypass state instead.A plugin can override this function to return a parameter which controls your plugin's bypass. You should always check the value of this parameter in your processBlock callback and bypass any effects if it is nonzero.