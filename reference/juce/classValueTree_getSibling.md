#### getSibling()


 ValueTree ValueTree::getSibling ( int delta ) const noexcept 
 

Returns one of this tree's siblings in its parent's child list.The delta specifies how far to move through the list, so a value of 1 would return the tree that follows this one, 1 would return the tree before it, 0 will return this one, etc. If the requested position is beyond the start or end of the child list, this will return an invalid object.