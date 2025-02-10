#### customComponentUsesTreeViewMouseHandler()


 virtual bool TreeViewItem::customComponentUsesTreeViewMouseHandler ( ) const virtual 
 

This should return true if you want to use a custom component, and also use the TreeView's builtin mouse handling support, enabling draganddrop, itemClicked() and itemDoubleClicked(); return false if the component should consume all mouse clicks.