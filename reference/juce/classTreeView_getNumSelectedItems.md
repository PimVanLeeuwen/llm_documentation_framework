#### getNumSelectedItems()


 int TreeView::getNumSelectedItems ( int maximumDepthToSearchTo = 1 ) const noexcept 
 

Returns the number of items that are currently selected.If maximumDepthToSearchTo is >= 0, it lets you specify a maximum depth to which the tree will be recursed.See alsogetSelectedItem, clearSelectedItems Referenced by FileTreeComponent::getNumSelectedFiles().