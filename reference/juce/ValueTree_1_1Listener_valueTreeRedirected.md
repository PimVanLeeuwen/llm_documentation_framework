#### valueTreeRedirected()


 virtual void ValueTree::Listener::valueTreeRedirected ( ValueTree & treeWhichHasBeenChanged ) virtual 
 

This method is called when a tree is made to point to a different internal shared object.When operator= is used to make a ValueTree refer to a different object, this callback will be made.