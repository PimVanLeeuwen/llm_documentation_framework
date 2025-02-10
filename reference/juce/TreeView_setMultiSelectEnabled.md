#### setMultiSelectEnabled()


 void TreeView::setMultiSelectEnabled ( bool canMultiSelect ) 
 

This sets a flag to indicate that the tree can be used for multiselection.You can always select multiple items internally by calling the TreeViewItem::setSelected() method, but this flag indicates whether the user is allowed to multiselect by clicking on the tree.By default it is disabled.See alsoisMultiSelectEnabled