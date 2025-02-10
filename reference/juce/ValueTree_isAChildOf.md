#### isAChildOf()


 bool ValueTree::isAChildOf ( const ValueTree & possibleParent ) const noexcept 
 

Returns true if this tree is a subtree (at any depth) of the given parent.This searches recursively, so returns true if it's a subtree at any level below the parent.