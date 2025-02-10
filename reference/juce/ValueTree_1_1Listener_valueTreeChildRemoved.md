#### valueTreeChildRemoved()


 virtual void ValueTree::Listener::valueTreeChildRemoved ( ValueTree & parentTree, ValueTree & childWhichHasBeenRemoved, int indexFromWhichChildWasRemoved ) virtual 
 

This method is called when a child subtree is removed.Note that when you register a listener to a tree, it will receive this callback for child changes in both that tree and any of its children, (recursively, at any depth). If your tree has subtrees but you only want to know about changes to the top level tree, just check the parentTree parameter to make sure it's the one that you're interested in.