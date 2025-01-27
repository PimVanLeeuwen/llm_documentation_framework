#### invoke()


 bool ApplicationCommandTarget::invoke ( const InvocationInfo & invocationInfo, 
 
 bool asynchronously ) 

Makes this target invoke a command.Your code can call this method to invoke a command on this target, but normally you'd call it indirectly via ApplicationCommandManager::invoke() or ApplicationCommandManager::invokeDirectly().If this target can perform the given command, it will call its perform() method to do so. If not, then getNextCommandTarget() will be used to determine the next target to try, and the command will be passed along to it.Parameters

 invocationInfo this must be correctly filledin, describing the context for the invocation. 
 
 asynchronously if false, the command will be performed before this method returns. If true, a message will be posted so that the command will be performed later on the message thread, and this method will return immediately. 



See alsoperform, ApplicationCommandManager::invoke