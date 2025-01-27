#### getHostedParameter()


 HostedParameter \* AudioPluginInstance::getHostedParameter ( int index ) const 
 

Gets the parameter at a particular index.If you want to find lots of parameters by their IDs, you should probably build and use a map<String, HostedParameter\*> by looping through all parameters.