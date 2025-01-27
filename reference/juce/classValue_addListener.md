#### addListener()


 void Value::addListener ( Listener \* listener ) 
 

Adds a listener to receive callbacks when the value changes.The listener is added to this specific Value object, and not to the shared object that it refers to. When this object is deleted, all the listeners will be lost, even if other references to the same Value still exist. So when you're adding a listener, make sure that you add it to a Value instance that will last for as long as you need the listener. In general, you'd never want to add a listener to a local stackbased Value, but more likely to one that's a member variable.See alsoremoveListener Referenced by StandalonePluginHolder::StandalonePluginHolder().