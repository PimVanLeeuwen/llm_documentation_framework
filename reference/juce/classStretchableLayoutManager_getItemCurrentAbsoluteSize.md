#### getItemCurrentAbsoluteSize()


 int StretchableLayoutManager::getItemCurrentAbsoluteSize ( int itemIndex ) const 
 

Returns the current size of one of the items.This is only meaningful after layOutComponents() has been called, as it returns the last size that this item was given. If the layout was done vertically, it'll return the item's height in pixels; if it was horizontal, it'll return its width.See alsogetItemCurrentRelativeSize