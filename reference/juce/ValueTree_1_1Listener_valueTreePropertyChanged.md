#### valueTreePropertyChanged()


 virtual void ValueTree::Listener::valueTreePropertyChanged ( ValueTree & treeWhosePropertyHasChanged, const Identifier & property ) virtual 
 

This method is called when a property of this tree (or of one of its subtrees) is changed.Note that when you register a listener to a tree, it will receive this callback for property changes in that tree, and also for any of its children, (recursively, at any depth). If your tree has subtrees but you only want to know about changes to the top level tree, simply check the tree parameter in this callback to make sure it's the tree you're interested in.