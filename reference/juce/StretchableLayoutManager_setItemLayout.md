#### setItemLayout()


 void StretchableLayoutManager::setItemLayout ( int itemIndex, 
 
 double minimumSize, 
 double maximumSize, 
 double preferredSize ) 

For a numbered item, this sets its size limits and preferred size.Parameters

 itemIndex the index of the item to change. 
 
 minimumSize the minimum size that this item is allowed to be a positive number indicates an absolute size in pixels. A negative number indicates a proportion of the available space (e.g 0.5 is 50%) 
 maximumSize the maximum size that this item is allowed to be a positive number indicates an absolute size in pixels. A negative number indicates a proportion of the available space 
 preferredSize the size that this item would like to be, if there's enough room. A positive number indicates an absolute size in pixels. A negative number indicates a proportion of the available space 



See alsogetItemLayout