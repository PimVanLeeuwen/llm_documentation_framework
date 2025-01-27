#### attachCallback()


 void ModalComponentManager::attachCallback ( Component \* component, 
 
 Callback \* callback ) 

Adds a new callback that will be called when the specified modal component is dismissed.If the component is modal, then when it is dismissed, either by being hidden, or by calling Component::exitModalState(), then the Callback::modalStateFinished() method will be called.Each component can have any number of callbacks associated with it, and this one is added to that list.The object that is passed in will be deleted by the manager when it's no longer needed. If the given component is not currently modal, the callback object is deleted immediately and no action is taken.