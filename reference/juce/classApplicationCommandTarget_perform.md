#### perform()


 virtual bool ApplicationCommandTarget::perform ( const InvocationInfo & info ) pure virtual 
 

This must actually perform the specified command.If this target is able to perform the command specified by the commandID field of the InvocationInfo structure, then it should do so, and must return true.If it can't handle this command, it should return false, which tells the caller to pass the command on to the next target in line.See alsoinvoke, ApplicationCommandManager::invoke Implemented in CodeEditorComponent, and JUCEApplication.