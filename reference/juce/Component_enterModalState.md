#### enterModalState()


 void Component::enterModalState ( bool takeKeyboardFocus = true, 
 
 ModalComponentManager::Callback \* callback = nullptr, 
 bool deleteWhenDismissed = false ) 

Puts the component into a modal state.This makes the component modal, so that messages are blocked from reaching any components other than this one and its children, but unlike runModalLoop(), this method returns immediately.If takeKeyboardFocus is true, the component will use grabKeyboardFocus() to get the focus, which is usually what you'll want it to do. If not, it will leave the focus unchanged.The callback is an optional object which will receive a callback when the modal component loses its modal status, either by being hidden or when exitModalState() is called. If you pass an object in here, the system will take care of deleting it later, after making the callback.If deleteWhenDismissed is true, then when it is dismissed, the component will be deleted and then the callback will be called. (This will safely handle the situation where the component is deleted before its exitModalState() method is called).See alsoexitModalState, runModalLoop, ModalComponentManager::attachCallback, ModalCallbackFunction