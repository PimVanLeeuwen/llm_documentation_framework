#### operator!=()


 bool ValueTree::operator!= ( const ValueTree & ) const noexcept 
 

Returns true if this and the other tree refer to different underlying structures.Note that this isn't a value comparison two independentlycreated trees which contain identical data are not considered equal.