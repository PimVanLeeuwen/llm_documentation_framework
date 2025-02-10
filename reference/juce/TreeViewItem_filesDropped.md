#### filesDropped()


 virtual void TreeViewItem::filesDropped ( const StringArray & files, int insertIndex ) virtual 
 

When files are dropped into this item, this callback is invoked.For this to work, you'll need to have also implemented isInterestedInFileDrag(). The insertIndex value indicates where in the list of subitems the files were dropped. If files are dropped onto an area of the tree where there are no visible items, this method is called on the root item of the tree, with an insert index of 0.See alsoFileDragAndDropTarget::filesDropped, isInterestedInFileDrag