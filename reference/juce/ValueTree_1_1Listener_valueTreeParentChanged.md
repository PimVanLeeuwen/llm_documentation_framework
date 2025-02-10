#### valueTreeParentChanged()


 virtual void ValueTree::Listener::valueTreeParentChanged ( ValueTree & treeWhoseParentHasChanged ) virtual 
 

This method is called when a tree has been added or removed from a parent.This callback happens when the tree to which the listener was registered is added or removed from a parent. Unlike the other callbacks, it applies only to the tree to which the listener is registered, and not to any of its children.