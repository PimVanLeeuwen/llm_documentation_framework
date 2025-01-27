#### addListener()


 void ValueTree::addListener ( Listener \* listener ) 
 

Adds a listener to receive callbacks when this tree is changed in some way.The listener is added to this specific ValueTree object, and not to the shared object that it refers to. When this object is deleted, all the listeners will be lost, even if other references to the same ValueTree still exist. And if you use the operator= to make this refer to a different ValueTree, any listeners will begin listening to changes to the new tree instead of the old one.When you're adding a listener, make sure that you add it to a ValueTree instance that will last for as long as you need the listener. In general, you'd never want to add a listener to a local stackbased ValueTree, and would usually add one to a member variable.See alsoremoveListener Referenced by CachedValue< Type >::CachedValue(), and CachedValue< Type >::CachedValue().