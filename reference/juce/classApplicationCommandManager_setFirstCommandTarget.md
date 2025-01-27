#### setFirstCommandTarget()


 void ApplicationCommandManager::setFirstCommandTarget ( ApplicationCommandTarget \* newTarget ) noexcept 
 

Sets a target to be returned by getFirstCommandTarget().If this is set to nullptr, then getFirstCommandTarget() will by default return the result of findDefaultComponentTarget().If you use this to set a target, make sure you call setFirstCommandTarget (nullptr) before deleting the target object.