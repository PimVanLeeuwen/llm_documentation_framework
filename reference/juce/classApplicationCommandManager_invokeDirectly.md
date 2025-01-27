#### invokeDirectly()


 bool ApplicationCommandManager::invokeDirectly ( CommandID commandID, 
 
 bool asynchronously ) 

Invokes the given command directly, sending it to the default target.This is just an easy way to call invoke() without having to fill out the InvocationInfo structure.