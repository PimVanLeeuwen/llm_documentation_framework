#### getItemCurrentRelativeSize()


 double StretchableLayoutManager::getItemCurrentRelativeSize ( int itemIndex ) const 
 

Returns the current size of one of the items.This is only meaningful after layOutComponents() has been called, as it returns the last size that this item was given. If the layout was done vertically, it'll return a negative value representing the item's height relative to the last size used for laying the components out; if the layout was done horizontally it'll be the proportion of its width.See alsogetItemCurrentAbsoluteSize