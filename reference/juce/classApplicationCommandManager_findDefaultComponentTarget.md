#### findDefaultComponentTarget()


 static ApplicationCommandTarget \* ApplicationCommandManager::findDefaultComponentTarget ( ) static 
 

Looks for a suitable command target based on which Components have the keyboard focus.This is used by the default implementation of ApplicationCommandTarget::getFirstCommandTarget(), but is exposed here in case it's useful.It tries to pick the best ApplicationCommandTarget by looking at focused components, top level windows, etc., and using the findTargetForComponent() method.