#### setRootItemVisible()


 void TreeView::setRootItemVisible ( bool shouldBeVisible ) 
 

Changes whether the tree's root item is shown or not.If the root item is hidden, only its subitems will be shown in the TreeView this lets you make the tree look as if it's got many root items. If it's hidden, this call will also make sure the root item is open (otherwise the TreeView would look empty).