#### valueTreeChildOrderChanged()


 virtual void ValueTree::Listener::valueTreeChildOrderChanged ( ValueTree & parentTreeWhoseChildrenHaveMoved, int oldIndex, int newIndex ) virtual 
 

This method is called when a tree's children have been reshuffled.Note that when you register a listener to a tree, it will receive this callback for child changes in both that tree and any of its children, (recursively, at any depth). If your tree has subtrees but you only want to know about changes to the top level tree, just check the parameter to make sure it's the tree that you're interested in.