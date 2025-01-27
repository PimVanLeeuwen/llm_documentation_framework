#### operator==()


 bool ValueTree::operator== ( const ValueTree & ) const noexcept 
 

Returns true if both this and the other tree refer to the same underlying structure.Note that this isn't a value comparison two independentlycreated trees which contain identical data are NOT considered equal.