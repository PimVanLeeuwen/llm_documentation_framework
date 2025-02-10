#### invoke()


 bool ApplicationCommandManager::invoke ( const ApplicationCommandTarget::InvocationInfo & invocationInfo, 
 
 bool asynchronously ) 

Sends a command to the default target.This will choose a target using getFirstCommandTarget(), and send the specified command to it using the ApplicationCommandTarget::invoke() method. This means that if the first target can't handle the command, it will be passed on to targets further down the chain (see ApplicationCommandTarget::invoke() for more info).Parameters

 invocationInfo this must be correctly filledin, describing the context for the invocation. 
 
 asynchronously if false, the command will be performed before this method returns. If true, a message will be posted so that the command will be performed later on the message thread, and this method will return immediately. 



See alsoApplicationCommandTarget::invoke