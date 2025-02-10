#### modalStateFinished()


 virtual void ModalComponentManager::Callback::modalStateFinished ( int returnValue ) pure virtual 
 

Called to indicate that a modal component has been dismissed.You can register a callback using Component::enterModalState() or ModalComponentManager::attachCallback().The returnValue parameter is the value that was passed to Component::exitModalState() when the component was dismissed.The callback object will be deleted shortly after this method is called.