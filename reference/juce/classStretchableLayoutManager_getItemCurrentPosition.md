#### getItemCurrentPosition()


 int StretchableLayoutManager::getItemCurrentPosition ( int itemIndex ) const 
 

Returns the current position of one of the items.This is only a valid call after layOutComponents() has been called, as it returns the last position that this item was placed at. If the layout was vertical, the value returned will be the y position of the top of the item, relative to the top of the rectangle in which the items were placed (so for example, item 0 will always have position of 0, even in the rectangle passed in to layOutComponents() wasn't at y = 0). If the layout was done horizontally, the position returned is the item's lefthand position, again relative to the x position of the rectangle used.See alsogetItemCurrentSize, setItemPosition