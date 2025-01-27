#### getChildWithName()


 ValueTree ValueTree::getChildWithName ( const Identifier & type ) const 
 

Returns the first subtree with the specified type name.If no such child tree exists, it'll return an invalid tree. (You can use isValid() to check whether a tree is valid)See alsogetOrCreateChildWithName